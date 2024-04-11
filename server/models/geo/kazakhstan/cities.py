from models.geo import Kazakhstan
from models.geo.city import City
from models.geo.name import Name
from models.geo.region import Region


class Semey(City):
    country_code = Kazakhstan.country_code
    name = Name(
        en='Semey',
        kk='Семей',
        ru='Семей'
    )


class Almaty(Region, City):
    country_code = Kazakhstan.country_code
    region_code = '02'
    type = Region.Type.CITY
    name = Name(
        en='Almaty city',
        kk='Алматы қаласы',
        ru='город Алматы'
    )
    short_name = Name(
        en='Almaty',
        kk='Алматы',
        ru='Алматы'
    )


class Astana(Region, City):
    country_code = Kazakhstan.country_code
    region_code = '01'
    type = Region.Type.CITY
    name = Name(
        en='Astana city',
        kk='Астана қаласы',
        ru='город Астана'
    )
    short_name = Name(
        en='Astana',
        kk='Астана',
        ru='Астана'
    )


class Baikonur(City):
    country_code = Kazakhstan.country_code
    type = Region.Type.CITY
    name = Name(
        en='Baikonur',
        kk='Байқоңыр қаласы',
        ru='город Байконур'
    )


class Shymkent(Region, City):
    country_code = Kazakhstan.country_code
    region_code = '17'
    type = Region.Type.CITY
    name = Name(
        en='Shymkent',
        kk='Шымкент қаласы',
        ru='город Шымкент'
    )
    short_name = Name(
        en='Shymkent',
        kk='Шымкент',
        ru='Шымкент'
    )
