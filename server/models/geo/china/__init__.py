from models.geo.country import Country
from models.geo.name import Name


class China(Country):
    icon = '🇨🇳'
    name = Name(
        en='China',
        kk='Қытай',
        ru='Китай'
    )
    country_code = 'CN'
    language_code = 'zh'
    phone_code = '86'
    phone_mask = '#### ####'
