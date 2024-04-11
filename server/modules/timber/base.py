import functools
import logging

from settings import settings


class Timber:
    class Formatter(logging.Formatter):
        pass

    class StreamHandler(logging.StreamHandler):
        pass

    ENABLED = settings.get('timber', {}).get('enabled', True)
    LEVEL = settings.get('timber', {}).get('level', 'DEBUG')
    logger = None

    flags = {}

    def __init__(self, name=None):
        if not self.ENABLED:
            logging.disable(logging.DEBUG)
        if self.logger is None:
            self.logger = logging.getLogger(name=name)
            self.logger.setLevel(logging.getLevelName(level=self.LEVEL))

    @staticmethod
    def basic_config(**kwargs):
        logging.basicConfig(**kwargs)

    @staticmethod
    def setup_packages(level, packages):
        for package in packages:
            logging.getLogger(name=package).setLevel(level=level)

    @staticmethod
    def get_level_name(level):
        return logging.getLevelName(level=level)

    def set_level(self, level):
        self.logger.setLevel(level=level)

    def add_handler(self, handler):
        self.logger.addHandler(handler)

    def d(self, msg, *args, **kwargs):
        return self._log(logging.debug.__name__, msg, *args, **kwargs)

    def i(self, msg, *args, **kwargs):
        return self._log(logging.info.__name__, msg, *args, **kwargs)

    def w(self, msg, *args, **kwargs):
        return self._log(logging.warning.__name__, msg, *args, **kwargs)

    def e(self, msg, *args, **kwargs):
        return self._log(logging.error.__name__, msg, *args, **kwargs)

    def x(self, msg, *args, **kwargs):
        return self._log(logging.exception.__name__, msg, *args, **kwargs)

    def c(self, msg, *args, **kwargs):
        return self._log(logging.critical.__name__, msg, *args, **kwargs)

    def _log(self, name: str, msg, *args, **kwargs):
        if name not in self.flags:
            if name == 'exception':
                name = 'error'
            self.flags[name] = self.logger.isEnabledFor(logging.getLevelName(name.upper()))
        if self.flags[name] is True:
            return self.__getattr__(name)(msg, *args, **kwargs)
        return None

    def __getattr__(self, attr):
        return functools.partial(getattr(self.logger, attr))


for level_name in (
    logging.getLevelName(logging.CRITICAL),
    logging.getLevelName(logging.FATAL),
    logging.getLevelName(logging.ERROR),
    logging.getLevelName(logging.WARNING),
    logging.getLevelName(logging.WARN),
    logging.getLevelName(logging.INFO),
    logging.getLevelName(logging.DEBUG),
    logging.getLevelName(logging.NOTSET)
):
    setattr(Timber, level_name, getattr(logging, level_name))
