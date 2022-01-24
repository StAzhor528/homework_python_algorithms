"""
Задание 6. На закрепление навыков работы с очередью
Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока
Реализуйте структуру "доска задач".
Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения
После реализации структуры, проверьте ее работу на различных сценариях
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""


class TaskQueue:
    def __init__(self):
        self.elems = {'base_queue': [], 'task_in_progress': [], 'solved_task': [], 'reworking': []}

    # функции для проверки на наличие, добавление в начало очереди, удаление последнего элемента,
    # проверки размера, просмотр содержимого списка очереди от куда беруться задачи.

    def is_empty_base(self):
        return self.elems['base_queue'] == []

    def to_queue_base(self, item):
        self.elems['base_queue'].insert(0, item)

    def from_queue_base(self):
        return self.elems['base_queue'].pop()

    def size_base(self):
        return len(self.elems['base_queue'])

    def show_base(self):
        return self.elems['base_queue']

    # функции для проверки на наличие, добавление в начало очереди, удаление последнего элемента,
    # проверки размера, просмотр содержимого списка очереди решаемых в данный момент задач.

    def is_empty_progress(self):
        return self.elems['task_in_progress'] == []

    def to_queue_progress(self, item):
        self.elems['task_in_progress'].insert(0, item)

    def from_queue_progress(self):
        return self.elems['task_in_progress'].pop()

    def size_progress(self):
        return len(self.elems['task_in_progress'])

    def show_progress(self):
        return self.elems['task_in_progress']

    # функции для проверки на наличие, добавление в начало очереди, удаление последнего элемента,
    # проверки размера, просмотр содержимого списка решенных задач.

    def is_empty_solved(self):
        return self.elems['solved_task'] == []

    def to_queue_solved(self, item):
        self.elems['solved_task'].insert(0, item)

    def from_queue_solved(self):
        return self.elems['solved_task'].pop()

    def size_solved(self):
        return len(self.elems['solved_task'])

    def show_solved(self):
        return self.elems['solved_task']

    # функции для проверки на наличие, добавление в начало очереди, удаление последнего элемента,
    # проверки размера, просмотр содержимого списка задач отправленных на доработку.

    def is_empty_reworking(self):
        return self.elems['reworking'] == []

    def to_queue_reworking(self, item):
        self.elems['reworking'].insert(0, item)

    def from_queue_reworking(self):
        return self.elems['reworking'].pop()

    def size_reworking(self):
        return len(self.elems['reworking'])

    def show_reworking(self):
        return self.elems['reworking']


if __name__ == '__main__':
    tq_obj = TaskQueue()
    print(tq_obj.is_empty_base())
    print(tq_obj.is_empty_progress())
    print(tq_obj.is_empty_solved())
    print(tq_obj.is_empty_reworking())

    tq_obj.to_queue_base(1)
    tq_obj.to_queue_progress(1)
    tq_obj.to_queue_solved(1)
    tq_obj.to_queue_reworking(1)

    print(tq_obj.show_base())
    print(tq_obj.show_progress())
    print(tq_obj.show_solved())
    print(tq_obj.show_reworking())

    tq_obj.to_queue_base(2)
    tq_obj.to_queue_progress(2)
    tq_obj.to_queue_solved(2)
    tq_obj.to_queue_reworking(2)

    print(tq_obj.show_base())
    print(tq_obj.show_progress())
    print(tq_obj.show_solved())
    print(tq_obj.show_reworking())

    print(tq_obj.from_queue_base())
    print(tq_obj.from_queue_progress())
    print(tq_obj.from_queue_solved())
    print(tq_obj.from_queue_reworking())

    print(tq_obj.show_base())
    print(tq_obj.show_progress())
    print(tq_obj.show_solved())
    print(tq_obj.show_reworking())
