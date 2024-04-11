from typing import Optional


class MetaError(type):
    def __new__(mcs, name, bases, attrs):
        e = super().__new__(mcs, name, bases, attrs)

        if bases:
            if 'code' not in attrs:
                raise NotImplementedError()

        e.name = name

        return e


class Error(metaclass=MetaError):
    code = -1
    message = None
    lang = 'ru'

    def __init__(self, **kwargs):
        if kwargs.get('message'):
            self.message = kwargs.pop('message')

        if kwargs.get('lang'):
            self.lang = kwargs.pop('lang')

        self.data = kwargs

    def get_message(self) -> Optional[str]:
        pass

    @property
    def parsed_message(self) -> Optional[str]:
        message = getattr(self, 'get_message')() if hasattr(self, 'get_message') else None

        if not message:
            message = self.message

        if message:
            try:
                return message.format(**self.data)
            except KeyError:
                return message

        return None

    def toDict(self) -> dict:
        return {
            'code': self.code,
            'name': self.name,
            'message': self.parsed_message,
            'params': self.data
        }

    def __str__(self) -> str:
        return f'{self.name}(code={self.code}, message={self.parsed_message}, data={self.data})'

    def __repr__(self) -> str:
        return str(self)


from .api import *
from .base import *
from .apps import *
