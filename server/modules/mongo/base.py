import logging
from motor import motor_asyncio

from settings import settings
from modules import Timber

timber = Timber('mongo')


class MongoProxy:
    db = None

    def __init__(self, url, loop):
        db_name = url.split('/')[-1]
        client = motor_asyncio.AsyncIOMotorClient(url, io_loop=loop)
        self.db = client[db_name]

    def __getattr__(self, item):
        return getattr(self.db, item)

    def __getitem__(self, item):
        return self.db[item]


class Mongo(dict):

    def initialize(self, loop):
        if not settings.get('mongo'):
            timber.w('No Mongo settings specified')
            return

        for key, url in settings['mongo'].items():
            timber.d(f'{key} {url}')
            self[key] = MongoProxy(url, loop)

    def __getattr__(self, item):
        return self[item]

