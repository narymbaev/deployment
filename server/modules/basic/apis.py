from typing import Optional

from .lists import ListUtils
from .strs import StrUtils


class APIRequestUtils:

    @staticmethod
    def to_list_of_ints(values, distinct=False) -> Optional[list]:
        output = StrUtils.to_str(values)
        output = ListUtils.to_list_of_ints(output.split(','), distinct=distinct) if output else None
        return output

    @staticmethod
    def to_list_of_strs(values, distinct=False) -> Optional[list]:
        output = StrUtils.to_str(values)
        output = ListUtils.to_list_of_strs(output.split(','), distinct=distinct) if output else None
        return output
