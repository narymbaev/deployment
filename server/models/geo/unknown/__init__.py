from models.geo.country import Country
from models.geo.name import Name


class Unknown(Country):
    icon = ''
    name = Name(
        en='Unknown',
        kk='Белгісіз',
        ru='Неопределенный'
    )
    country_code = ''
    language_code = ''
    phone_code = ''
    phone_mask = ''
