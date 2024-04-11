from typing import Optional

import asyncpg

from modules.basic.strs import StrUtils


def get_user_display_name(user) -> Optional[str]:
    if user:
        if isinstance(user, dict) or isinstance(user, asyncpg.Record):
            return ' '.join(
                StrUtils.to_str(user.get(field), default='')
                for field in ['last_name', 'first_name', 'patronymic']
            ).strip()
    return None
