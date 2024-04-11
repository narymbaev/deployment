from .base_enum import *


class _FileStatus(BaseEnumModel):
    PENDING = BaseEnumItem(id=1, name='В очереди', key='pending')
    STARTED = BaseEnumItem(id=2, name='В работе', key='started')
    FINISHED = BaseEnumItem(id=3, name='Завершён', key='finished')
    ERROR = BaseEnumItem(id=4, name='Ошибка', key='error')
    EMPTY = BaseEnumItem(id=5, name='Нет записей', key='empty')
    # TIMEOUT = BaseEnumItem(id=6, name='Превышено время ожидания', key='timeout')


FileStatus = _FileStatus()
