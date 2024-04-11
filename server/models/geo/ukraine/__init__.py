from models.geo.country import Country
from models.geo.name import Name


class Ukraine(Country):
    icon = '🇺🇦'
    name = Name(
        en='Ukraine',
        kk='Украина',
        ru='Украина'
    )
    country_code = 'UA'
    language_code = 'uk'
    phone_code = '380'
    phone_mask = '## ### ## ##'
