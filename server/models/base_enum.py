
__all__ = ['BaseEnumModel', 'BaseEnumItem']


class BaseEnumItem:
    def __init__(self, **kwargs):
        self.keys = []

        for key, val in kwargs.items():
            self.keys.append(key)
            self.__setattr__(key, val)

    def __str__(self):
        return str({key: self.__getattribute__(key) for key in self.keys})

    def __getattr__(self, item):
        try:
            super().__getattribute__()
        except:
            pass

    def get(self, key):
        return self.__getattribute__(key)

    def to_dict(self):
        return {
            key: self.get(key) for key in self.keys
        }


class BaseEnumModel:
    fields = None

    def __init__(self):
        self.cases: {str: BaseEnumItem} = {}
        for key, case in self.__class__.__dict__.items():
            if not key.isupper():  # Takes only UPPER case named attributes
                continue

            if not self.fields:
                self.fields = case.keys.copy()
                for field in self.fields:
                    self.__setattr__(field+'_to_object', {})
            case.__name__ = key.lower()
            self.cases[key] = case

            for field in self.fields:
                self.__getattribute__(field+'_to_object')[case.get(field)] = case

    def __str__(self):
        return self.__class__.__name__ + '[' + ','.join(list(self.cases.keys())) + ']'

    def of(self, field, value):
        return self.__getattribute__(field+'_to_object').get(value)

    def to_json(self):
        return [case.to_dict() for case in self.cases.values()]
