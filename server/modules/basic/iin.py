import traceback
from datetime import date, datetime
from typing import Optional

from models.sex import Sex
from modules.basic.regexp import RegExp


class IIN:

    @staticmethod
    def is_valid(iin) -> bool:
        return RegExp.is_valid_iin(iin)

    def __init__(self, value):
        if not IIN.is_valid(value):
            raise ValueError('Invalid IIN!')
        self.value = value

    @classmethod
    def _normalize_int(cls, value):
        return int(value.lstrip('0') or 0)

    def _parse_year(self):
        year = self._normalize_int(self.value[0:2])
        if year > int(str(datetime.now().year)[2:4]):
            return int(f'19{year}')
        else:
            return int(f'20{str(year).zfill(2)}')

    def _parse_month(self):
        return self._normalize_int(self.value[2:4])

    def _parse_day(self):
        return self._normalize_int(self.value[4:6])

    def parse_birthdate(self) -> Optional[date]:
        try:
            return date(
                year=self._parse_year(),
                month=self._parse_month(),
                day=self._parse_day()
            )
        except (Exception,):
            traceback.print_exc()
            return None

    def parse_sex(self) -> Sex:
        sex = int(self.value[6])
        if sex % 2 == 0:
            return Sex.FEMALE
        return Sex.MALE

    def __str__(self):
        return f'IIN(value={self.value})'

    def __repr__(self):
        return str(self)
