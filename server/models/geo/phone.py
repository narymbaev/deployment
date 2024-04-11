from models.geo import Azerbaijan, China, Georgia, Greece, Kazakhstan, Kyrgyzstan, Russia, Tajikistan, Turkey, \
    Uzbekistan
from models.geo.cyprus import Cyprus
from models.geo.israel import Israel
from models.geo.ukraine import Ukraine
from models.locale import Locale
from modules.basic.phones import PhoneNumberUtils

COUNTRY_CODE = {
    7: (Kazakhstan(), Russia(),),
    8: (Kazakhstan(),),
    30: (Greece(),),
    357: (Cyprus(),),
    380: (Ukraine(),),
    86: (China(),),
    90: (Tajikistan(),),
    972: (Israel(),),
    992: (Turkey(),),
    994: (Azerbaijan(),),
    995: (Georgia(),),
    996: (Kyrgyzstan(),),
    998: (Uzbekistan(),),
}


async def get_phone_info(value) -> dict:
    country = PhoneNumberUtils.parse_country(value)
    if not country:
        return {}

    # length = len(country.phone_mask.replace(' ', '') + country.phone_code)
    # if len(value) != length:
    #     return {}

    return {
        'country_info': {
            'value': value,
            **country.to_dict(Locale.default())
        }
    }
