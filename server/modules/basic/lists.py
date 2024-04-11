from typing import List, Optional, Tuple

import itertools

from .dicts import DictUtils
from .ints import IntUtils
from .strs import StrUtils


class ListUtils:

    @staticmethod
    def to_list(value):
        if value and isinstance(value, list):
            return value
        return None

    @staticmethod
    def distinct(value) -> Optional[list]:
        if value and isinstance(value, list):
            return list(set(value))
        return None

    @staticmethod
    def append(elements, item) -> Optional[list]:
        if elements and isinstance(elements, list):
            if item not in elements:
                elements.append(item)
        return elements

    @staticmethod
    def remove(elements, item) -> Optional[list]:
        if elements and isinstance(elements, list):
            if item in elements:
                elements.remove(item)
        return elements

    @staticmethod
    def to_list_of_ints(value, distinct=False) -> List[int]:
        if value and isinstance(value, list):
            output = []
            for item in value:
                converted = IntUtils.to_int(item)
                if isinstance(converted, int):
                    if distinct:
                        if converted in output:
                            continue
                    output.append(converted)
            return output if output else []
        return []

    @staticmethod
    def to_list_of_strs(value, distinct=False) -> Optional[List[str]]:
        if value and isinstance(value, list):
            output = []
            for item in value:
                converted = StrUtils.to_str(item)
                if converted:
                    if distinct:
                        if converted in output:
                            continue
                    output.append(converted)
            return output if output else None
        return None

    @staticmethod
    def to_list_of_dicts(value, clean=False) -> List[dict]:
        output = []
        if value and isinstance(value, list):
            for item in value:
                if clean:
                    output.append(DictUtils.validate_dict(dict(item)))
                else:
                    output.append(dict(item))
        return output

    @staticmethod
    def unpack_list_and_total(value, total_field='over_total') -> Tuple[list, int]:
        over_total = value and total_field in value[0] and value[0][total_field] or 0
        output = [{
            k: v
            for k, v in i.items()
            if k != total_field
        } for i in value] if over_total else [dict(i) for i in value]
        return output, over_total

    @staticmethod
    def depth(value) -> int:
        if value and isinstance(value, list):
            return 1 + max(ListUtils.depth(item) for item in value)
        return 0

    @staticmethod
    def group_by(value, attr) -> Optional[dict]:
        grouped = {}
        if value and isinstance(value, list):
            for i, j in itertools.groupby(value):
                if not hasattr(i, attr):
                    continue
                v = getattr(i, attr)
                if not grouped.get(v):
                    grouped[v] = []
                grouped[v].extend(list(j))
        return grouped
