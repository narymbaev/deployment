from models.geo.country import Country
from models.geo.name import Name


class Israel(Country):
    icon = '🇮🇱'
    name = Name(
        en='Israel',
        kk='Израиль',
        ru='Израиль'
    )
    country_code = 'IL'
    language_code = 'il'
    phone_code = '972'
    phone_mask = '## ### ## ##'
