from . import Error


class UserNotFoundError(Error):
    code = 5004
    message = 'Пользователь не найден в системе'


class ProjectNotFoundError(Error):
    code = 5006
    message = 'Проект не найден в системе'


class TaskNotFoundError(Error):
    code = 5000
    message = 'Задача не найдена в системе'


class UserIINNotFoundError(Error):
    code = 5016
    message = 'У пользователя нет ИИН'


class TaskTrackIDNotFoundError(Error):
    code = 5017
    message = 'Не найден трек-номер задачи'


class UnableToDeleteUsers(Error):
    code = 5018
    message = 'Не удалось удалить пользователей с id: {user_ids}'


class DeleteUserSpecifiedAsFormAssignee(Error):
    code = 5001
    message = 'Пользователь назначен как исполнитель задачи в форме(-ах). ' \
              'Пожалуйста, перед удалением сперва отвяжите сотрудника из форм(-ы) с id: {form_ids}'


class DeleteUserSpecifiedAsProjectParticipant(Error):
    code = 5002
    message = 'Пользователь является участником проект(-ов). ' \
              'Пожалуйста, перед удалением сперва исключите сотрудника из проект(-ов) с {projects}'


class RatingListWithEmptyCriterion(Error):
    code = 5003
    message = 'Оценочный лист не может быть пустым, добавьте критерии оценки'


class OperationFailed(Error):
    code = 5005
    message = 'Операция не выполнена'


class SIPTaken(Error):
    code = 5008
    message = 'Вы не можете присвоить этот SIP ID, так как он присвоен оператору {user}'


class FolderNotEmpty(Error):
    code = 5009
    message = 'Категория должна быть пустой!'


class TitleRepeated(Error):
    code = 5010
    message = 'Наименование не должно повторяться'


class InvalidIINFormatError(Error):
    code = 5011
    message = 'Неверный формат ИИН ({format}): {iin}'


class InvalidPhoneNumberFormatError(Error):
    code = 5012
    message = 'Неверный формат номера телефона ({format}): {phone}'


class TaskInvalidAssignee(Error):
    code = 5013
    message = 'Неверные данные исполнителя(-ей)'


class ExternalAPIError(Error):
    code = 5014
    message = 'Ошибка внешнего API'


class SurveyExpired(Error):
    code = 5015
    message = '{reason}'


class ProjectIsNotEmpty(Error):
    code = 5016
    message = 'В проекте присутствуют задачи'


class TechSupportLimit(Error):
    code = 5017
    message = 'Превышен суточный лимит по заявкам'


class ReportTypeNotFound(Error):
    code = 5019
    message = 'Отчёт не найден в системе'
