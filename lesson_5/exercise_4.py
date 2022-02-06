"""
Задача 4.
Создайте обычный словарь и упорядоченный словарь OrderedDict.
Выполните операции, равные по смыслу, с каждым из словарей и сделайте замеры.
Опишите полученные результаты, сделайте выводы
И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях
"""

from collections import OrderedDict
from timeit import timeit

od = OrderedDict()
d = {}


def add_od():
    for i in range(100000):
        od[i] = i


def add_d():
    for i in range(100000):
        d[i] = i


def change_od():
    for i in range(100000):
        od[i] = i + 1


def change_d():
    for i in range(100000):
        d[i] = i + 1


def mte_od():
    for i in range(100000):
        od.move_to_end(i)


def mte_d():
    for i in range(100000):
        d.pop(i)
        d[i] = i


def popitem_od():
    for i in range(100000):
        od.popitem(last=True)


def popitem_d():
    for i in range(100000):
        d.popitem()


def pop_od():
    for i in range(100000):
        od.pop(i)


def pop_d():
    for i in range(100000):
        d.pop(i)


print('Время выполнения операции добавления элемента:')
print('Для OrderedDict - ', timeit("add_od()", "from __main__ import add_od", number=1))
print('Для обычного словаря - ', timeit("add_d()", "from __main__ import add_d", number=1))

print('Время выполнения операции замены элемента:')
print('Для OrderedDict - ', timeit("change_od()", "from __main__ import change_od", number=1))
print('Для обычного словаря - ', timeit("change_d()", "from __main__ import change_d", number=1))

print('Время выполнения операции перемещения элемента в конец:')
print('Для OrderedDict - ', timeit("mte_od()", "from __main__ import mte_od", number=1))
print('Для обычного словаря - ', timeit("mte_d()", "from __main__ import mte_d", number=1))

print('Время выполнения операции удаления элемента:')
print('Для OrderedDict - ', timeit("pop_od()", "from __main__ import pop_od", number=1))
print('Для обычного словаря - ', timeit("pop_d()", "from __main__ import pop_d", number=1))

add_d()
add_od()

print('Время выполнения операции удаления пары ключ значение:')
print('Для OrderedDict - ', timeit("popitem_od()", "from __main__ import popitem_od", number=1))
print('Для обычного словаря - ', timeit("popitem_d()", "from __main__ import popitem_d", number=1))

# Вывод:
# 1) В большинстве методов словарь работает быстрее, чем OrderedDict, кроме метода move_to_end.
# Этот метод еще хорош тем, что можем перемещать пары непосредственно в начало списка, тогда как для словаря для этого
# потребуется больше строчек кода.
# 2) Для перемещения пары ключ/значение из начала в конец или наоборот, лучше использовать OrderedDict.popitem,
# так как данный способ более лаконичен чем со словарем.
