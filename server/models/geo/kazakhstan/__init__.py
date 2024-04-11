from models.geo.country import Country
from models.geo.name import Name


class Kazakhstan(Country):
    icon = '🇰🇿'
    name = Name(
        en='Kazakhstan',
        kk='Қазақстан',
        ru='Казахстан'
    )
    country_code = 'KZ'
    language_code = 'kk'
    phone_code = '7'
    phone_mask = '### ### ## ##'
