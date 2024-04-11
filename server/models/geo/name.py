from models.locale import Locale


class Name:
    en = None
    kk = None
    ru = None

    def __init__(self, kk, ru, en=None):
        self.en = en
        self.kk = kk
        self.ru = ru

    def get(self, locale=Locale.default()):
        return getattr(self, locale.language)


class ShortName(Name):
    pass
