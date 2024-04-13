class Output:
    message = None

    def __repr__(self):
        return self.message

    def __str__(self):
        return self.message


from .api import *
from .base import *
from .telegram import *
