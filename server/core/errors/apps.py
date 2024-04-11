from . import Error


class ApiKeysDeactivated(Error):
    code = 500
    message = 'Ключи деактивированные из-за ошибки: {keys_list}'
