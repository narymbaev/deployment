from enum import Enum, unique
from typing import Optional


@unique
class MobileNetworkOperator(Enum):
    ALTEL = ['700', '708']
    BEELINE = ['705', '706', '771', '776', '777']
    KCELL = ['701', '702', '775', '778']
    TELE2 = ['707', '747']

    @staticmethod
    def by(value) -> Optional['MobileNetworkOperator']:
        for mno in MobileNetworkOperator:
            if value in mno.value:
                return mno
        return None

    @staticmethod
    def values() -> list:
        values = []
        for mno in MobileNetworkOperator:
            values.extend(mno.value)
        return values

    # Example: '708' in MobileNetworkOperator.ALTEL
    def __contains__(self, item) -> bool:
        if item and isinstance(item, str):
            if item in self.value:
                return True
        return False
