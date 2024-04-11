import traceback
from typing import Optional

import ujson


class JSONUtils:

    @staticmethod
    def to_dict(value) -> Optional[dict]:
        if value and isinstance(value, str):
            pass
        else:
            return None
        try:
            return ujson.loads(value)
        except (Exception,):
            traceback.print_exc()
        return None

    @staticmethod
    def to_list(value) -> Optional[list]:
        if value and isinstance(value, str):
            pass
        else:
            return None
        try:
            return ujson.loads(value)
        except (Exception,):
            traceback.print_exc()
        return None
