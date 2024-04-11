class Language:
    _LANG_IDS = {'ru': 1, 'kk': 2, 'en': 3}
    _LANG_CODES = {1: 'ru', 2: 'kk', 3: 'en'}

    DEFAULT_ID = 1
    DEFAULT_CODE = 'ru'

    id = None
    code = None

    def __init__(self, lang):
        lang = self.normalize(lang)
        self.code = lang if lang in self._LANG_IDS else self.DEFAULT_CODE
        self.id = self._LANG_IDS.get(lang, self.DEFAULT_ID)

    @staticmethod
    def of(lang, default=None) -> 'Language':
        if lang and isinstance(lang, str):
            if lang in ['kk', 'kz', 'ru', 'en']:
                return Language(lang)
        if default and isinstance(default, Language):
            return default
        return Language(Language.DEFAULT_CODE)

    @staticmethod
    def normalize(lang):
        if not lang:
            return Language.DEFAULT_CODE
        if lang and isinstance(lang, str):
            if lang == 'kz':
                return 'kk'
        return lang

    def __str__(self):
        return self.code

    def __repr__(self):
        return self.code

    @staticmethod
    def code_by_id(lang_id):
        return Language._LANG_CODES[lang_id]

    @staticmethod
    def id_by_code(lang_code):
        return Language._LANG_IDS.get(lang_code)
