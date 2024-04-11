from collections import OrderedDict
from typing import Optional
from typing import Tuple

from models.calls.mno import MobileNetworkOperator
from models.geo import Geo
from .lists import ListUtils
from .regexp import RegExp


class PhoneNumberUtils:

    @staticmethod
    def parse_country(phone) -> Optional[dict]:
        if phone and isinstance(phone, str):
            phone = phone.lstrip('+')
            if not phone:
                return None

            if len(phone) == 11 and phone.startswith('8'):
                phone = '7' + phone[1:]

            grouped = ListUtils.group_by(Geo.COUNTRIES, 'phone_code')
            grouped = OrderedDict(sorted(grouped.items(), reverse=True))

            c = 1
            while not grouped.get(phone[0:c]):
                c += 1
                if c == len(str(max(grouped.keys()))) + 1:
                    break

            countries = grouped.get(phone[0:c])
            if not countries:
                return None

            return countries[0]
        return None

    @staticmethod
    def normalize(value, strict=True) -> Optional[str]:
        if value and isinstance(value, str):
            if value == 'anonymous':
                return None

            value = ''.join(filter(str.isnumeric, value))

            if len(value) == 10:
                value = f'7{value}'
            elif len(value) == 11 and value.startswith('8'):
                value = f'7{value[1:]}'

            if strict:
                if RegExp.is_valid_phone(value):
                    return value
            else:
                return value

        return None

    @staticmethod
    def sanitize(value) -> Optional[str]:
        if value and isinstance(value, str):
            return ''.join(filter(str.isnumeric, value))
        return None

    @staticmethod
    def get_variants(value) -> list:
        if value and isinstance(value, str):
            return [i for i in [value, value[1:], f'7{value[1:]}', f'7{value}', f'8{value[1:]}']]
        return []

    @staticmethod
    def parse(value) -> Tuple[Optional[str], Optional[str]]:
        if not value:
            return None, None

        digits = value[-10:]
        prefix = digits[:3]

        if prefix not in MobileNetworkOperator.values():
            return None, None

        return MobileNetworkOperator.by(prefix).name, f'7{digits}'
