from models.geo.country import Country
from models.geo.name import Name


class Turkey(Country):
    icon = '🇹🇷'
    name = Name(
        en='Turkey',
        kk='Түркия',
        ru='Турция'
    )
    country_code = 'TR'
    language_code = 'tu'
    phone_code = '90'
    phone_mask = '### ### ## ##'
