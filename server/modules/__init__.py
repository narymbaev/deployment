
from .timber import Timber  # noqa: E402
timber = Timber('reports')


from .mongo import Mongo  # noqa: E402
mongo = Mongo()


from .psql import PSQL  # noqa: E402
db = PSQL()


from .cache import Cache  # noqa: E402
cache = Cache()
