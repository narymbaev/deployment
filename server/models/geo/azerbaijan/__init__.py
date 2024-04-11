from models.geo.country import Country
from models.geo.name import Name


class Azerbaijan(Country):
    icon = '🇦🇿'
    name = Name(
        en='Azerbaijan',
        kk='Әзірбайжан',
        ru='Азербайджан'
    )
    country_code = 'AZ'
    language_code = 'aj'
    phone_code = '994'
    phone_mask = '## ### ## ##'
