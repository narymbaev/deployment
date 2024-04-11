from models.geo.azerbaijan import Azerbaijan
from models.geo.china import China
from models.geo.cyprus import Cyprus
from models.geo.georgia import Georgia
from models.geo.greece import Greece
from models.geo.israel import Israel
from models.geo.kazakhstan import Kazakhstan
from models.geo.kazakhstan.cities import Almaty as AlmatyCity, Astana, Baikonur, Shymkent
from models.geo.kazakhstan.regions import Abai, Akmola, Aktobe, Almaty as AlmatyRegion, Atyrau, EastKazakhstan, \
    Jambyl, Jetisu, Karaganda, Kostanay, Kyzylorda, Mangystau, NorthKazakhstan, Pavlodar, Turkistan, Ulytau, \
    WestKazakhstan
from models.geo.kyrgyzstan import Kyrgyzstan
from models.geo.russia import Russia
from models.geo.serbia import Serbia
from models.geo.tajikistan import Tajikistan
from models.geo.turkey import Turkey
from models.geo.ukraine import Ukraine
from models.geo.unknown import Unknown
from models.geo.uzbekistan import Uzbekistan


class Geo:
    COUNTRIES = [
        Azerbaijan(),
        China(),
        Cyprus(),
        Israel(),
        Georgia(),
        Greece(),
        Kazakhstan(),
        Kyrgyzstan(),
        Russia(),
        Serbia(),
        Tajikistan(),
        Turkey(),
        Ukraine(),
        Uzbekistan(),
        Unknown(),
    ]

    REGIONS = [
        Abai(),
        Akmola(),
        Aktobe(),
        AlmatyRegion(),
        Atyrau(),
        EastKazakhstan(),
        Jambyl(),
        Jetisu(),
        Karaganda(),
        Kostanay(),
        Kyzylorda(),
        Mangystau(),
        NorthKazakhstan(),
        Pavlodar(),
        Turkistan(),
        Ulytau(),
        WestKazakhstan(),
    ]

    @staticmethod
    def get_regions(country_code):
        if country_code == Kazakhstan.country_code:
            return [
                Abai(),
                Akmola(),
                Aktobe(),
                AlmatyRegion(),
                AlmatyCity(),
                Astana(),
                Atyrau(),
                EastKazakhstan(),
                Jambyl(),
                Jetisu(),
                Karaganda(),
                Kostanay(),
                Kyzylorda(),
                Mangystau(),
                NorthKazakhstan(),
                Pavlodar(),
                Shymkent(),
                Turkistan(),
                Ulytau(),
                WestKazakhstan(),
            ]
        return None
