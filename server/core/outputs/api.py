from core.outputs import Output


class TaskCreated(Output):
    message = 'Задача создана'


class TaskDeleted(Output):
    message = 'Задача удалена'


class TaskArchived(Output):
    message = 'Задача заархивирована'


class TaskCompleted(Output):
    message = 'Задача завершена'


class TaskSenderChanged(Output):
    message = 'Автор задачи изменен'


class TaskSubscribed(Output):
    message = 'Подписался на задачу'


class TaskUnsubscribed(Output):
    message = 'Отписался от задачи'


class MentionLiked(Output):
    message = 'Отметка "Нравится"'
