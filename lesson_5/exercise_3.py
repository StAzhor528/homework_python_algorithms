"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно
что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list
Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.
1) сравнить операции
append, pop, extend списка и дека и сделать выводы что и где быстрее
2) сравнить операции
appendleft, popleft, extendleft дека и соответствующих им операций списка
и сделать выводы что и где быстрее
3) сравнить операции получения элемента списка и дека
и сделать выводы что и где быстрее
Подсказка:
для того, чтобы снизить погрешность, желательно операции по каждой ф-ции
(append, pop и т.д.) проводить в циклах. Для замеров используйте timeit.
"""
from timeit import timeit
from collections import deque

our_lst = []
our_dq = deque()


# 1) сравнить операции
# append, pop, extend списка и дека и сделать выводы что и где быстрее

def app_lst(lst, el):
    for i in range(100000):
        lst.append(el)


def app_dq(dq, el):
    for i in range(100000):
        dq.append(el)


def pop_lst(lst):
    for i in range(100000):
        lst.pop()


def pop_dq(dq):
    for i in range(100000):
        dq.pop()


def extend_lst(lst, items):
    for i in range(100000):
        lst.extend(items)


def extend_dq(dq, items):
    for i in range(100000):
        dq.extend(items)


# 2) сравнить операции appendleft, popleft, extendleft дека и соответствующих им операций списка
# и сделать выводы что и где быстрее.

def insert_lst(lst, el):
    for i in range(1000):
        lst.insert(0, el)


def appleft_dq(dq, el):
    for i in range(1000):
        dq.appendleft(el)


def del_lst(lst):
    for i in range(1000):
        del lst[0]


def popleft_dq(dq):
    for i in range(1000):
        dq.popleft()


def extleft_lst(lst, items):
    for i in range(1000):
        for el in items:
            lst.insert(0, el)


def extleft_dq(dq, items):
    for i in range(1000):
        dq.extendleft(items)


# 3) сравнить операции получения элемента списка и дека
# и сделать выводы что и где быстрее

def getel_lst(lst):
    for i in range(10000):
        lst[0]


def getel_dq(dq):
    for i in range(10000):
        dq[0]


print('Время выполнения операций append, pop, extend со списком:')
print('append - ', timeit("app_lst(our_lst, 3)", "from __main__ import app_lst, our_lst", number=1))
print('pop - ', timeit("pop_lst(our_lst)", "from __main__ import pop_lst, our_lst", number=1))
print('extend - ', timeit("extend_lst(our_lst, [1, 2])", "from __main__ import extend_lst, our_lst", number=1))

print('Время выполнения операций append, pop, extend с деком:')
print('append - ', timeit("app_dq(our_dq, 3)", "from __main__ import app_dq, our_dq", number=1))
print('pop - ', timeit("pop_dq(our_dq)", "from __main__ import pop_dq, our_dq", number=1))
print('extend - ', timeit("extend_dq(our_dq, [1, 2])", "from __main__ import extend_dq, our_dq", number=1))

print('Время выполнения операций insert в начало, del из начала и insert элементов списка в начало со списком:')
print('insert - ', timeit("insert_lst(our_lst, 3)", "from __main__ import insert_lst, our_lst", number=1))
print('del - ', timeit("del_lst(our_lst)", "from __main__ import del_lst, our_lst", number=1))
print('insert списка - ', timeit("extleft_lst(our_lst, [1, 2])", "from __main__ import extleft_lst, our_lst", number=1))

print('Время выполнения операций appendleft, popleft, extendleft с деком:')
print('appendleft - ', timeit("appleft_dq(our_dq, 3)", "from __main__ import appleft_dq, our_dq", number=1))
print('popleft - ', timeit("popleft_dq(our_dq)", "from __main__ import popleft_dq, our_dq", number=1))
print('extendleft - ', timeit("extleft_dq(our_dq, [1, 2])", "from __main__ import extleft_dq, our_dq", number=1))

print('Время выполнения операции получения элемента списка:')
print(timeit("getel_lst(our_lst)", "from __main__ import getel_lst, our_lst", number=1))

print('Время выполнения операции получения элемента дека:')
print(timeit("getel_dq(our_dq)", "from __main__ import getel_dq, our_dq", number=1))

# Вывод:
# 1) Операции append, pop, extend со списком и деком отрабатывают прибоизительно за одно и тоже время.
# 2) Операций appendleft, popleft, extendleft с деком отрабатывают на несколько порядков быстрее,
# чем аналогичные операции со списком.
# 3) Время выполнения операции получения элемента списка гораздо быстрее, чем операция получения элемента дека.
