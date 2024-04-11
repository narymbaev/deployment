from typing import Optional


class FloatUtils:

    @staticmethod
    def to_float(value, default=None) -> Optional[float]:
        if isinstance(value, float):
            return value
        elif isinstance(value, str):
            if value.replace('.', '').isdigit():
                return float(value)
            elif value.startswith('-') and value[1:].replace('.', '').isdigit():
                return float(value)
        if isinstance(default, float):
            return default
        return None

    @staticmethod
    def calculate_percentage(a, b) -> float:
        if isinstance(a, int) or isinstance(a, float):
            if isinstance(b, int) or isinstance(b, float):
                if a == 0 or b == 0:
                    return 0
                return FloatUtils.pretty_percentage(a / b * 100) or 0
        return 0

    @staticmethod
    def pretty_percentage(value) -> Optional[float]:
        if isinstance(value, int) or isinstance(value, float):
            return round(value, 2)
        return None

    @staticmethod
    def format_percentage(value) -> Optional[str]:
        if isinstance(value, int) or isinstance(value, float):
            return '{:.1f}'.format(value)
        return None
