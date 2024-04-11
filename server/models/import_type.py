from .base_enum import *


class _ImportType(BaseEnumModel):
    """
    Типы отчётов обязательны к заполнению
    При редактировании продублируйте в оба проекта:
        - qbox-backend
        - qbox-imports
    """
    SALES = BaseEnumItem(name='Воронка продаж', key='sales')


ImportType = _ImportType()
