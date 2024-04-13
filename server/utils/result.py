from typing import Optional, Union

from core.errors import Error

__all__ = ['Result', 'AnyResult']


class Result:
    class Success:
        def __init__(self, data: dict):
            self.data = data
            assert self.data and isinstance(self.data, dict)

        def get_data(self) -> Optional[dict]:
            return self.data

        def __str__(self):
            return f'{self.__class__.__name__}(data={self.data})'

        def __repr__(self):
            return str(self)

    class Error:
        def __init__(self, error: Error):
            self.error = error
            assert self.error and isinstance(self.error, Error)

        def __str__(self):
            return f'{self.__class__.__name__}(error={self.error})'

        def __repr__(self):
            return str(self)

    def get_data(self) -> dict:
        if isinstance(self, Result.Success):
            if self.data:
                return self.data
        return {}

    def require_data(self) -> Optional[dict]:
        if isinstance(self, Result.Success):
            return self.data
        raise ValueError()

    def __repr__(self):
        return str(self)

    def __str__(self) -> str:
        if isinstance(self, Result.Success):
            return str(self.data)
        elif isinstance(self, Result.Error):
            return str(self.error)
        else:
            return str(self)


AnyResult = Union[Result, Result.Success, Result.Error]
