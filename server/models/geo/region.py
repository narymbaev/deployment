import enum

from models.geo.name import Name
from models.locale import Locale


class Region:
    @enum.unique
    class Type(enum.Enum):
        REGION = 'region'
        CITY = 'city'

    country_code: str = None
    region_code: str = None
    type: Type = None
    name: Name = None
    short_name: Name = None

    def __init__(self):
        if not self.short_name:
            self.short_name = self.name

    def to_dict(self, locale=Locale.default()) -> dict:
        return {
            'name': self.name.get(locale),
            'short_name': self.short_name.get(locale),
            'country': {
                'code': self.country_code
            },
            'code': self.region_code,
            'type': self.type.value
        }
