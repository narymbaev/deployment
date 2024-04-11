from models.geo.country import Country
from models.geo.name import Name


class Georgia(Country):
    icon = '🇬🇪'
    name = Name(
        en='Georgia',
        kk='Грузия',
        ru='Грузия'
    )
    country_code = 'GE'
    language_code = 'ka'
    phone_code = '995'
    phone_mask = '## ### ## ##'
