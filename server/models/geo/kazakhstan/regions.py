from models.geo.kazakhstan import Kazakhstan
from models.geo.name import Name
from models.geo.region import Region


class Abai(Region):
    country_code = Kazakhstan.country_code
    region_code = '18'
    type = Region.Type.REGION
    name = Name(
        en='Abai Region',
        kk='Абай облысы',
        ru='Абайская область',
    )


class Akmola(Region):
    country_code = Kazakhstan.country_code
    region_code = '03'
    type = Region.Type.REGION
    name = Name(
        en='Akmola Region',
        kk='Ақмола облысы',
        ru='Акмолинская область',
    )


class Aktobe(Region):
    country_code = Kazakhstan.country_code
    region_code = '04'
    type = Region.Type.REGION
    name = Name(
        en='Aktobe Region',
        kk='Ақтөбе облысы',
        ru='Актюбинская область',
    )


class Almaty(Region):
    country_code = Kazakhstan.country_code
    region_code = '05'
    type = Region.Type.REGION
    name = Name(
        en='Almaty Region',
        kk='Алматы облысы',
        ru='Алматинская область',
    )


class Atyrau(Region):
    country_code = Kazakhstan.country_code
    region_code = '06'
    type = Region.Type.REGION
    name = Name(
        en='Atyrau Region',
        kk='Атырау облысы',
        ru='Атырауская область',
    )


class EastKazakhstan(Region):
    country_code = Kazakhstan.country_code
    region_code = '16'
    type = Region.Type.REGION
    name = Name(
        en='East Kazakhstan Region',
        kk='Шығыс Қазақстан облысы',
        ru='Восточно-Казахстанская область',
    )


class Jambyl(Region):
    country_code = Kazakhstan.country_code
    region_code = '08'
    type = Region.Type.REGION
    name = Name(
        en='Jambyl Region',
        kk='Жамбыл облысы',
        ru='Жамбылская область',
    )


class Jetisu(Region):
    country_code = Kazakhstan.country_code
    region_code = '19'
    type = Region.Type.REGION
    name = Name(
        en='Jetisu Region',
        kk='Жетісу облысы',
        ru='Жетысуская область',
    )


class Karaganda(Region):
    country_code = Kazakhstan.country_code
    region_code = '09'
    type = Region.Type.REGION
    name = Name(
        en='Karaganda Region',
        kk='Қарағанды облысы',
        ru='Карагандинская область',
    )


class Kostanay(Region):
    country_code = Kazakhstan.country_code
    region_code = '10'
    type = Region.Type.REGION
    name = Name(
        en='Kostanay Region',
        kk='Қостанай облысы',
        ru='Костанайская область',
    )


class Kyzylorda(Region):
    country_code = Kazakhstan.country_code
    region_code = '11'
    type = Region.Type.REGION
    name = Name(
        en='Kyzylorda Region',
        kk='Қызылорда облысы',
        ru='Кызылординская область',
    )


class Mangystau(Region):
    country_code = Kazakhstan.country_code
    region_code = '12'
    type = Region.Type.REGION
    name = Name(
        en='Mangystau Region',
        kk='Маңғыстау облысы',
        ru='Мангыстауская область',
    )


class NorthKazakhstan(Region):
    country_code = Kazakhstan.country_code
    region_code = '15'
    type = Region.Type.REGION
    name = Name(
        en='North Kazakhstan Region',
        kk='Солтүстік Қазақстан облысы',
        ru='Северо-Казахстанская область',
    )


class Pavlodar(Region):
    country_code = Kazakhstan.country_code
    region_code = '14'
    type = Region.Type.REGION
    name = Name(
        en='Pavlodar Region',
        kk='Павлодар облысы',
        ru='Павлодарская область',
    )


class Turkistan(Region):
    country_code = Kazakhstan.country_code
    region_code = '13'
    type = Region.Type.REGION
    name = Name(
        en='Turkistan Region',
        kk='Түркістан облысы',
        ru='Туркестанская область',
    )


class Ulytau(Region):
    country_code = Kazakhstan.country_code
    region_code = '20'
    type = Region.Type.REGION
    name = Name(
        en='Ulytau Region',
        kk='Ұлытау облысы',
        ru='Улытауская область',
    )


class WestKazakhstan(Region):
    country_code = Kazakhstan.country_code
    region_code = '07'
    type = Region.Type.REGION
    name = Name(
        en='West Kazakhstan Region',
        kk='Батыс Қазақстан облысы',
        ru='Западно-Казахстанская область',
    )
