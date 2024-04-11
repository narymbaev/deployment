from models.geo.country import Country
from models.geo.name import Name


class Serbia(Country):
    icon = '🇷🇸'
    name = Name(
        en='Serbia',
        kk='Сербия',
        ru='Сербия'
    )
    country_code = 'RS'
    language_code = 'sr'
    phone_code = '381'
    phone_mask = '## ### ####'