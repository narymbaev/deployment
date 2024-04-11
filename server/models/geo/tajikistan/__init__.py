from models.geo.country import Country
from models.geo.name import Name


class Tajikistan(Country):
    icon = '🇹🇯'
    name = Name(
        en='Tajikistan',
        kk='Тәжікстан',
        ru='Таджикистан'
    )
    country_code = 'TJ'
    language_code = 'ti'
    phone_code = '992'
    phone_mask = '## ### ## ##'
