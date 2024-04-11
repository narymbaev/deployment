import os

from app import app
from modules import timber

import logging
logging.basicConfig(level=logging.DEBUG)


is_debug = timber.logger.level == timber.DEBUG
timber.basic_config(level=timber.get_level_name(os.getenv('LOG_LEVEL', timber.logger.level)))
# timber.setup_packages(timber.WARNING, [
#     'aio_pika', 'aiormq', 'aioredis', 'cache', 'psql', 'mongo'
# ])

if __name__ == '__main__':

    app.set_config(
        ROOT_PATH=os.path.dirname(__file__),
        IS_DEBUG=is_debug
    )
    try:
        app.run('0.0.0.0', port=9977, access_log=False)
    except Exception as e:
        print(e)
