from typing import Optional


class BoolUtils:

    @staticmethod
    def as_bool(value, default=None) -> Optional[bool]:
        if isinstance(value, bool):
            return value
        if isinstance(default, bool):
            return default
        return None

    @staticmethod
    def to_bool(value, default=None) -> Optional[bool]:
        if isinstance(value, bool):
            return value
        if isinstance(value, int):
            if value == 0:
                return False
            elif value == 1:
                return True
        if isinstance(value, str):
            value = value.lower()
            if value == '1' or value == 'true':
                return True
            elif value == '0' or value == 'false':
                return False
        if isinstance(default, bool):
            return default
        return None
