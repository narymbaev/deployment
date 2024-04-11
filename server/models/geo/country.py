from models.geo.name import Name
from models.locale import Locale


class Country:
    icon: str = None
    name: Name = None
    short_name: Name = None
    country_code: str = None
    language_code: str = None
    phone_code: str = None
    phone_mask: str = None
    phone_placeholder: str = None

    def __init__(self):
        if self.phone_mask and isinstance(self.phone_mask, str):
            if not self.phone_placeholder:
                self.phone_placeholder = self.phone_mask.replace('#', 'X')

        if not self.short_name:
            self.short_name = self.name

    def to_dict(self, locale=Locale.default()) -> dict:
        return {
            'icon': self.icon,
            'name': self.name.get(locale),
            'short_name': self.short_name.get(locale),
            'code': self.country_code,
            'language': {
                'code': self.language_code,
            },
            'phone': {
                'code': self.phone_code,
                'mask': self.phone_mask,
                'placeholder': self.phone_placeholder,
            },
        }
