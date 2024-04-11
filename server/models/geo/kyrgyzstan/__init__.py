from models.geo.country import Country
from models.geo.name import Name


class Kyrgyzstan(Country):
    icon = '🇰🇬'
    name = Name(
        en='Kyrgyzstan',
        kk='Қырғызстан',
        ru='Кыргызстан'
    )
    country_code = 'KG'
    language_code = 'ky'
    phone_code = '996'
    phone_mask = '## ### ## ##'
