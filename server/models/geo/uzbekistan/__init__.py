from models.geo.country import Country
from models.geo.name import Name


class Uzbekistan(Country):
    icon = '🇺🇿'
    name = Name(
        en='Uzbekistan',
        kk='Өзбекстан',
        ru='Узбекистан'
    )
    country_code = 'UZ'
    language_code = 'uz'
    phone_code = '998'
    phone_mask = '## ### ## ##'
