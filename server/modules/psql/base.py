
import asyncpg
import ujson

from settings import settings
from modules import Timber

timber = Timber('psql')


class PSQL:
    pool = None

    @staticmethod
    async def pool_connection_init(connection):
        for json_type in ['json', 'jsonb']:
            await connection.set_type_codec(
                json_type,
                encoder=ujson.dumps,
                decoder=ujson.loads,
                schema='pg_catalog'
            )

    async def initialize(self, loop):
        if not settings.get('psql'):
            timber.w('No PSQL settings specified')
            return
        self.pool = await asyncpg.create_pool(
            database=settings['psql'].get('database'),
            host=settings['psql'].get('host'),
            port=settings['psql'].get('port'),
            user=settings['psql'].get('user'),
            password=settings['psql'].get('password'),
            init=self.pool_connection_init,
            min_size=10,
            max_size=15,
            command_timeout=600,
            loop=loop
        )

    async def execute(self, *args, **kwargs):
        self.log('execute', *args, **kwargs)
        async with self.pool.acquire() as connection:
            return await connection.execute(*args, **kwargs)

    async def fetch(self,*args, **kwargs):
        self.log('fetch', *args, **kwargs)
        async with self.pool.acquire() as connection:
            return await connection.fetch(*args, **kwargs)

    async def fetchrow(self, *args, **kwargs):
        self.log('fetchrow', *args, **kwargs)
        async with self.pool.acquire() as connection:
            return await connection.fetchrow(*args, **kwargs)

    async def fetchval(self, *args, **kwargs):
        self.log('fetchval', *args, **kwargs)
        async with self.pool.acquire() as connection:
            return await connection.fetchval(*args, **kwargs)

    @staticmethod
    def log(method, *args, **kwargs):
        if not timber.logger.getEffectiveLevel() == timber.DEBUG:
            return

        query = ' '.join(filter(lambda item: item and item != '\n', args[0].replace('\n', ' ').split(' ')))
        params = args[1:]
        log_text = f'{method}({query})'
        if params:
            log_text += f' | {params}'
        if kwargs:
            log_text += f' | {kwargs}'
        timber.d(log_text)
