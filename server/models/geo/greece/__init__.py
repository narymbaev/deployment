from models.geo.country import Country
from models.geo.name import Name


class Greece(Country):
    icon = '🇬🇷'
    name = Name(
        en='Greece',
        kk='Греция',
        ru='Греция'
    )
    country_code = 'GR'
    language_code = 'el'
    phone_code = '30'
    phone_mask = '### ### ####'
