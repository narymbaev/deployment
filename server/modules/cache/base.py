
import functools
import aio_pika
import aioredis
import ujson

from settings import settings
from modules import Timber

timber = Timber('cache')


class Cache:

    def __init__(self):
        self.pool = None
        self.channel = None
        self.loop = None

    async def initialize(self, loop):
        self.loop = loop

        self.pool = await aioredis.create_redis_pool(
            settings['redis'],
            db=1,
            loop=loop,
            encoding='utf-8'
        )

        connection = await aio_pika.connect_robust(
            settings['mq'], loop=loop
        )

        self.channel = await connection.channel()

    def __getattr__(self, attr):
        return functools.partial(getattr(self.pool, attr))

    async def queue(self, queue, data):
        try:
            await self.publish(queue, data)
        except Exception as e:
            timber.x(e)
            timber.d(f'Cache$queue() -> [FAILED] queue: {queue}, data: {data}')
            await self.publish(queue, data)

    async def publish(self, queue, data):
        await self.channel.default_exchange.publish(
            aio_pika.Message(
                body=bytes(data, 'utf-8')
            ),
            routing_key=queue
        )

    async def trigger(self, event_name, **data):
        data['_event'] = event_name
        await self.queue('ch:events', ujson.dumps(data))

    def multi_exec(self):
        return self.pool.multi_exec()

