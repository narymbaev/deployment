import asyncpg
from datetime import datetime
from typing import Optional

from core import errors
from core.helpers import Sender
from data import RepositoryResponse

from models.channel import Channel
from models.language import Language
from models.sex import Sex
from modules import db, timber
from modules.basic.datetimes import DatetimeUtils
from modules.basic.dicts import DictUtils
from modules.basic.emails import EmailUtils
from modules.basic.iin import IIN
from modules.basic.ints import IntUtils
from modules.basic.lists import ListUtils
from modules.basic.phones import PhoneNumberUtils
from modules.basic.regexp import RegExp
from modules.basic.strs import StrUtils

_customers_repository_instance = None


class CustomersRepository:

    @classmethod
    def instance(cls):
        global _customers_repository_instance
        if not _customers_repository_instance:
            _customers_repository_instance = cls()
        return _customers_repository_instance

    @classmethod
    def _transform_projection_to_fields(cls, projection) -> str:
        if projection and isinstance(projection, dict):
            projection['id'] = True  # Must-have field
            return ', '.join([k for k, v in projection.items() if v is True])
        return 'id'

    async def get(self, id, projection=None) -> Optional[asyncpg.Record]:
        # Projection
        fields = self._transform_projection_to_fields(projection)

        return await db.fetchrow(
            '''
            SELECT {fields}
            FROM forms.client_users
            WHERE id = $1
            '''.format(
                fields=fields
            ),
            id
        )

    async def search(
        self,
        first_name=None,
        last_name=None,
        patronymic=None,
        iin=None,
        phone=None,
        projection=None
    ) -> Optional[asyncpg.Record]:
        # Projection
        fields = self._transform_projection_to_fields(projection or {'*': True})
        customer = None

        if iin:  # Search by IIN
            customer = await db.fetchrow(
                '''
                SELECT {fields}
                FROM forms.client_users
                WHERE iin = $1
                ORDER BY id
                '''.format(fields=fields),
                iin
            )
            if customer:
                return customer

        if phone:  # Fallback to search by phone
            customer = await db.fetchrow(
                '''
                SELECT {fields}
                FROM forms.client_users
                WHERE phone = ANY($1) OR contacts ->> 'sip' = ANY($1)
                ORDER BY id
                '''.format(fields=fields),
                PhoneNumberUtils.get_variants(phone)
            )
            if customer:
                return customer

        # Last fallback to search by full name
        if first_name and last_name and patronymic:
            customer = await db.fetchrow(
                '''
                SELECT {fields}
                FROM forms.client_users
                WHERE first_name = $1 AND last_name = $2 AND patronymic = $3
                ORDER BY id
                '''.format(fields=fields),
                first_name,
                last_name,
                patronymic
            )

        return customer

    async def insert(
        self,
        employee_id,
        origin,
        params,
        projection=None
    ) -> RepositoryResponse:
        timber.d(f'insert() -> {origin}, {params}, {projection}')

        if origin == 'manual':
            return await self._insert_manual_customer(employee_id, params, projection)

        return False, errors.InvalidValue(parameter='origin', value=origin)

    async def update(
        self,
        employee_id,
        origin,
        params,
        projection=None
    ) -> RepositoryResponse:
        timber.d(f'CustomersRepository#update() -> {origin}, {params}, {projection}')

        if origin == 'manual':
            return await self._manual_customer_update(employee_id, params, projection)

        return False, errors.InvalidValue(parameter='origin', value=origin)

    async def get_customer_by_id(self, customer_id, projection=None) -> Optional[asyncpg.Record]:
        # Projection
        fields = self._transform_projection_to_fields(projection)

        customer_id = IntUtils.to_int(customer_id)
        if not customer_id:
            timber.w(f'CustomersRepository#get_customer_by_id() -> [customer_id cannot be converted] {customer_id}')
            return None

        return await db.fetchrow(
            '''
            SELECT {fields}
            FROM forms.client_users
            WHERE id = $1
            '''.format(
                fields=fields
            ),
            customer_id
        )

    async def _manual_customer_update(
        self,
        employee_id,
        params,
        projection=None,
    ) -> RepositoryResponse:
        customer_id = IntUtils.to_int(params.get('id'))
        if not customer_id:
            return False, errors.InvalidValue(parameter='id', value=params.get('id'))

        sender = Sender.of(StrUtils.to_str(params.get('sender')))
        first_name = StrUtils.to_str(params.get('first_name'))
        last_name = StrUtils.to_str(params.get('last_name'))
        patronymic = StrUtils.to_str(params.get('patronymic'))
        iin = IIN(params['iin']) if RegExp.is_valid_iin(params.get('iin')) else None
        phone = PhoneNumberUtils.sanitize(params.get('phone'))
        email = EmailUtils.normalize(params.get('email'))
        sex = IntUtils.to_int(params.get('sex'))
        birthdate = DatetimeUtils.str_2_datetime(params.get('birthdate'), '%d.%m.%Y')
        country_id = IntUtils.to_int(params.get('country_id'))
        region_id = IntUtils.to_int(params.get('region_id'))
        city_id = IntUtils.to_int(params.get('city_id'))
        photo = StrUtils.to_str(params.get('photo'))
        language = Language(StrUtils.to_str(params.get('language')))
        extra_emails = ListUtils.to_list_of_strs(params.get('extra_emails'), distinct=True)
        extra_phones = ListUtils.to_list_of_strs(params.get('extra_phones'), distinct=True)
        details = DictUtils.validate_dict(params.get('details')) or {}

        search_projection = {
            'id': True,
            'first_name': True,
            'last_name': True,
            'patronymic': True,
            'iin': True,
            'phone': True,
            'contacts': True,
        }

        if first_name:
            if 1 <= len(first_name) <= 200:
                pass
            else:
                return False, errors.InvalidTextLength(field='Имя', min=1, max=200)
        else:
            return False, errors.RequiredField(field='first_name: str')

        if last_name:
            if 1 <= len(last_name) <= 200:
                pass
            else:
                return False, errors.InvalidTextLength(field='Фамилия', min=1, max=200)

        if patronymic:
            if 1 <= len(patronymic) <= 200:
                pass
            else:
                return False, errors.InvalidTextLength(field='Отчество', min=1, max=200)

        # Projection
        fields = self._transform_projection_to_fields(projection)

        # Birthdate & sex
        if iin:
            search = await self.search(iin=iin.value, projection=search_projection)
            if search and customer_id != search.get('id'):
                return False, errors.DuplicateRecord(
                    customer=search,
                    message=f'Клиент с таким ИИН ({iin.value}) уже существует. Дубликат не может быть создан'
                )
            else:
                if not birthdate:
                    birthdate = iin.parse_birthdate()

                if Sex.is_valid_sex(sex):
                    pass
                else:
                    sex = iin.parse_sex().value

        # Contacts
        contacts = {}

        if sender:
            contacts[sender.channel] = sender.id

            if sender.channel == Channel.SIP.value:
                phone = PhoneNumberUtils.normalize(sender.id)
            elif sender.channel == Channel.WEBSOCKET.value:
                if email:
                    sender = Sender(f'user:{Channel.EMAIL.value}:{email}')
                elif phone:
                    sender = Sender(f'user:{Channel.SIP.value}:{phone}')

        if email:
            if not sender:
                sender = Sender(f'user:{Channel.EMAIL.value}:{email}')

            if Channel.EMAIL.value not in contacts:
                contacts[Channel.EMAIL.value] = email

        if not iin and phone:
            search = await self.search(phone=phone, projection=search_projection)
            if search and customer_id != search.get('id'):
                return False, errors.DuplicateRecord(
                    customer=search,
                    message=f'Клиент с таким номером телефона ({phone}) уже существует. Дубликат не может быть создан'
                )
            else:
                if not sender:
                    sender = Sender(f'user:{Channel.SIP.value}:{phone}')

                if Channel.SIP.value not in contacts:
                    contacts[Channel.SIP.value] = phone

        if extra_emails:
            details['extra_emails'] = [{'email': i} for i in extra_emails]

        if extra_phones:
            details['extra_phones'] = [{'number': PhoneNumberUtils.sanitize(i)} for i in extra_phones]

        customer = await self.get_customer_by_id(customer_id=customer_id, projection={'*': True})

        if customer:
            is_customer_verified = customer.get('flags', [0, 0, 0, 0, 0])[4]
            if is_customer_verified:
                is_customer_verification_field_updated = False

                # TODO: Bad code
                if customer['first_name'] != first_name:
                    is_customer_verification_field_updated = True

                if customer['last_name'] != last_name:
                    is_customer_verification_field_updated = True

                if customer['patronymic'] != patronymic:
                    is_customer_verification_field_updated = True

                if customer['iin'] != (iin.value if iin else None):
                    is_customer_verification_field_updated = True

                if is_customer_verification_field_updated:
                    await db.execute(
                        '''
                        UPDATE forms.client_users 
                        SET flags[5] = 0
                        WHERE id = $1
                        ''',
                        customer['id']
                    )

        updated_customer = await db.fetchrow(
            '''
            UPDATE forms.client_users
            SET 
                first_name = $2, 
                last_name = $3,
                patronymic = $4, 
                sex = $5,
                birth_date = $6,
                birthday = $7,
                photo = $8,
                iin = $9,
                phone = $10,
                email = $11,
                lang = $12,
                locale = $13,
                contacts = $14,
                country_id = $15,
                region_id = $16,
                city_id = $17,
                details = $18
            WHERE id = $1
            RETURNING {fields}
            '''.format(
                fields=fields
            ),
            customer['id'],
            first_name if first_name else StrUtils.to_str(customer['first_name']),
            last_name if last_name else StrUtils.to_str(customer['last_name']),
            patronymic if patronymic else StrUtils.to_str(customer['patronymic']),
            sex if isinstance(sex, int) and sex in [0, 1] else customer['sex'],
            birthdate if birthdate else customer['birth_date'],
            birthdate if birthdate else customer['birth_date'],
            photo if photo else StrUtils.to_str(customer['photo']),
            iin.value if iin else StrUtils.to_str(customer['iin']),
            phone if phone else PhoneNumberUtils.normalize(customer['phone']),
            email if email else EmailUtils.normalize(customer['email']),
            language.id,
            language.code,
            contacts,
            country_id,
            region_id,
            city_id,
            details
        )

        if not updated_customer:
            return False, errors.OperationFailed()

        # await Audit.instance().invoke(
        #     employee_id=employee_id,
        #     event=Audit.Event.CUSTOMER_UPDATE,
        #     object_id=updated_customer['id'],
        #     old=dict(customer),
        #     new=dict(updated_customer)
        # )

        # await trigger_customer_change(updated_customer['id'])

        updated_customer = dict(updated_customer)

        updated_customer['sender'] = sender.address if sender else Sender(f'user:id:{updated_customer["id"]}').address

        return True, updated_customer

    # async def upsert(
    #     self,
    #     origin,
    #     params,
    #     projection=None,
    # ) -> RepositoryResponse:
    #     timber.d(f'upsert() -> {origin}, {params}, {projection}')
    #
    #     if origin == 'bridge':
    #         return await self._upsert_bridge_customer(params, projection)
    #     elif origin == 'chat-bot':
    #         return await self._upsert_chat_bot_customer(params, projection)
    #
    #     return False, errors.InvalidValue(parameter='origin', value=origin)

    # TODO
    async def _insert_manual_customer(
        self,
        employee_id,
        params,
        projection=None,
    ) -> RepositoryResponse:
        first_name = StrUtils.to_str(params.get('first_name'))
        last_name = StrUtils.to_str(params.get('last_name'))
        patronymic = StrUtils.to_str(params.get('patronymic'))
        sender = Sender.of(StrUtils.to_str(params.get('sender')))
        sex = IntUtils.to_int(params.get('sex'))
        iin = IIN(params['iin']) if RegExp.is_valid_iin(params.get('iin')) else None
        phone = PhoneNumberUtils.sanitize(params.get('phone'))
        extra_emails = ListUtils.to_list_of_strs(params.get('extra_emails'), distinct=True)
        extra_phones = ListUtils.to_list_of_strs(params.get('extra_phones'), distinct=True)
        birthdate = DatetimeUtils.str_2_datetime(params.get('birthdate'), '%d.%m.%Y')
        email = EmailUtils.normalize(params.get('email'))
        language = Language(StrUtils.to_str(params.get('language')))
        photo = StrUtils.to_str(params.get('photo'))
        country_id = IntUtils.to_int(params.get('country_id'))
        region_id = IntUtils.to_int(params.get('region_id'))
        city_id = IntUtils.to_int(params.get('city_id'))
        details = DictUtils.validate_dict(params.get('details')) or {}

        if not first_name:
            return False, errors.RequiredField(field='first_name: str')

        # Projection
        fields = self._transform_projection_to_fields(projection)

        search_projection = {
            'id': True,
            'first_name': True,
            'last_name': True,
            'patronymic': True,
            'iin': True,
            'phone': True,
            'contacts': True,
        }

        # Search
        if iin:
            customer = await self.search(iin=iin.value, projection=search_projection)
            if customer:
                return False, errors.DuplicateRecord(
                    customer=customer,
                    message='Клиент с таким ИИН уже существует. Дубликат не может быть создан'
                )

        if phone:
            customer = await self.search(phone=phone, projection=search_projection)
            if customer:
                return False, errors.DuplicateRecord(
                    customer=customer,
                    message='Клиент с таким номером телефона уже существует. Дубликат не может быть создан'
                )

        customer = await self.search(
            first_name=first_name,
            last_name=last_name,
            patronymic=patronymic,
            projection=search_projection
        )
        if customer:
            return False, errors.DuplicateRecord(
                customer=customer,
                message='Клиент с таким ФИО уже существует. Дубликат не может быть создан'
            )

        # Birthdate & sex
        if iin:
            if not birthdate:
                birthdate = iin.parse_birthdate()

            if sex == -1:
                sex = iin.parse_sex().value

        # Contacts
        contacts = {}

        if sender:
            contacts[sender.channel] = sender.id

            if sender.channel == Channel.SIP.value:
                phone = PhoneNumberUtils.normalize(sender.id)
            elif sender.channel == Channel.WEBSOCKET.value:
                if email:
                    sender = Sender(f'user:{Channel.EMAIL.value}:{email}')
                elif phone:
                    sender = Sender(f'user:{Channel.SIP.value}:{phone}')

        if email:
            if not sender:
                sender = Sender(f'user:{Channel.EMAIL.value}:{email}')

            if Channel.EMAIL.value not in contacts:
                contacts[Channel.EMAIL.value] = email

        if phone:
            if not sender:
                sender = Sender(f'user:{Channel.SIP.value}:{phone}')

            if Channel.SIP.value not in contacts:
                contacts[Channel.SIP.value] = phone

        if extra_emails:
            details['extra_emails'] = [{'email': i} for i in extra_emails]

        if extra_phones:
            details['extra_phones'] = [{'number': PhoneNumberUtils.sanitize(i)} for i in extra_phones]

        inserted_customer = await db.fetchrow(
            '''
            INSERT INTO forms.client_users(
                first_name,
                last_name,
                patronymic,
                sex,
                birth_date,
                photo,
                iin,
                phone,
                email,
                lang,
                locale,
                device,
                contacts,
                country_id,
                region_id,
                city_id,
                details,
                created_at,
                created_by
            )
            VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13, $14, $15, $16, $17, $18, $19)
            ON CONFLICT DO NOTHING
            RETURNING {fields}
            '''.format(
                fields=fields
            ),
            first_name,
            last_name,
            patronymic,
            sex if sex in [0, 1] else -1,
            birthdate if birthdate else datetime.now(),
            photo,
            iin.value if iin else None,
            phone,
            email,
            language.id,
            language.code,
            sender.address if sender else None,
            contacts,
            country_id,
            region_id,
            city_id,
            details,
            datetime.now(),
            employee_id
        )

        if not inserted_customer:
            return False, errors.OperationFailed()

        # await Audit.instance().invoke(
        #     employee_id=employee_id,
        #     event=Audit.Event.CUSTOMER_CREATE,
        #     object_id=inserted_customer['id'],
        #     new=dict(inserted_customer)
        # )

        # await trigger_customer_change(inserted_customer['id'])

        inserted_customer = dict(inserted_customer)

        inserted_customer['sender'] = sender.address if sender else Sender(f'user:id:{inserted_customer["id"]}').address

        return True, inserted_customer