from models.geo.country import Country
from models.geo.name import Name


class Russia(Country):
    icon = '🇷🇺'
    name = Name(
        en='Russian Federation',
        kk='Ресей Федерациясы',
        ru='Российская Федерация'
    )
    short_name = Name(
        en='Russia',
        kk='Ресей',
        ru='Россия'
    )
    country_code = 'RU'
    language_code = 'ru'
    phone_code = '7'
    phone_mask = '### ### ## ##'
