from typing import Optional

from modules.basic.regexp import RegExp


class EmailUtils:

    @staticmethod
    def normalize(value) -> Optional[str]:
        if value and isinstance(value, str):
            value = value.strip()
            if RegExp.is_valid_email(value):
                return value
        return None
