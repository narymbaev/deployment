from typing import Optional


class Locale:
    _DEFAULT = None

    def __init__(
        self,
        _id: int,
        language: str,
        region: Optional[str],
        title: str,
        description: Optional[str] = None,
        priority: Optional[int] = None
    ):
        self.id = _id
        self.language = language
        self.region = region
        self.title = title
        self.description = description
        self.priority = priority

    @staticmethod
    def default() -> 'Locale':
        if not Locale._DEFAULT:
            Locale._DEFAULT = Locale(
                _id=1,
                language='ru',
                region='RU',
                title='Русский язык',
                description=None,
                priority=None
            )
        return Locale._DEFAULT

    def to_dict(self):
        return {
            'id': self.id,
            'language': self.language,
            'region': self.region,
            'title': self.title,
            'description': self.description,
            'priority': self.priority,
        }

    def __str__(self) -> str:
        if self.region:
            return '{}.{}'.format(self.language, self.region)
        return self.language

    def __repr__(self) -> str:
        return str(self)
