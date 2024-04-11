# from i18n import i18n
from . import Error


class Unknown(Error):
    code = 1
    message = 'Произошла неизвестная ошибка'


class InvalidAuth(Error):
    code = 2
    message = 'Ошибка аутентификации (некорректные входные данные)'


class RequiredParams(Error):
    code = 3
    message = 'Ожидаемые параметры не были переданы'


class RequiredField(Error):
    code = 4
    message = 'Отсуствуют обязательные параметры "{field}"'

    # def get_message(self):
    #     return i18n.get_string('required_field_empty', self.lang)


class RequiredFields(Error):
    code = 5
    message = 'Отсуствуют обязательные параметры "{fields}"'


class IllegalState(Error):
    code = 6
    message = 'Приложение находится в неподходящем состоянии для запрошенной операции'


class InvalidAction(Error):
    code = 7
    message = 'Неверное действие'


class PermissionDenied(Error):
    code = 8
    message = 'В доступе отказано'

    # def get_message(self):
    #     return i18n.get_string('error.permission_denied', self.lang)


class ExternalAPIFailure(Error):
    code = 9
    message = 'Ошибка в внешнем API: {cause}'


class UnsupportedCondition(Error):
    code = 10
    message = 'Извините, на данный момент поддерживается только "{parameter}"'


class NetworkConnection(Error):
    code = 11
    message = 'Ошибка сети'


class NotFound(Error):
    code = 12
    message = '{item} не найден(-o, -а) в системе'


class DuplicateRecord(Error):
    code = 13
    message = '{item} с этими значениями уже существует. Дубликат не может быть создан'


class Deleted(Error):
    code = 14
    message = '"{item}" удален(-о, -а) из системы'

    # def get_message(self):
    #     return i18n.get_string('error.deleted', self.lang)


class Blocked(Error):
    code = 15
    message = '"{item}" заблокирован(-о, -а) в системе'

    # def get_message(self):
    #     return i18n.get_string('error.blocked', self.lang)


class InvalidValue(Error):
    code = 16
    message = 'Неверное значение "{value}" для параметра "{parameter}"'


class UpdateRestricted(Error):
    code = 17
    message = 'Редактирование запрещено: {reason}'


class Deprecated(Error):
    code = 18
    message = 'Версия API устарела'


class DayOff(Error):
    code = 19
    message = 'Если этот день является выходным полностью, то активируйте опцию "Выходной день, а если этот день является сокращенным, то установите время начала и время завершения'

    # def get_message(self):
    #     return i18n.get_string('is_day_off', self.lang)


class WrongTime(Error):
    code = 20
    message = 'Нельзя установить праздничный график с такими параметрами: время завершения меньше время начала'

    # def get_message(self):
    #     return i18n.get_string('wrong_time', self.lang)


class InvalidTime(Error):
    code = 21
    message = 'Неверное время'


class InvalidBreak(Error):
    code = 22
    message = 'Неверное время перерыва'


class InvalidTextLength(Error):
    code = 23
    message = 'Поле "{field}" должен содержать более {min} и менее {max} символов'
