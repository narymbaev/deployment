from typing import Tuple, Union

from core import errors

RepositoryResponse = Tuple[bool, Union[list, dict, errors.Error]]
