from models.geo.country import Country
from models.geo.name import Name


class Cyprus(Country):
    icon = '🇨🇾'
    name = Name(
        en='Cyprus',
        kk='Кипр',
        ru='Кипр'
    )
    country_code = 'CY'
    language_code = 'el'
    phone_code = '357'
    phone_mask = '## ### ###'
