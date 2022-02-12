"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.
Решите задачу тремя способами:
1) с помощью сортировки, которую мы не рассматривали на уроке (Гномья, Шелла,
Кучей)
сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""
from random import randint
from timeit import timeit


def dwarf_sort(lst):
    i = 0
    n = len(lst)
    while i + 1 < n:
        if lst[i + 1] >= lst[i]:
            i += 1
        else:
            lst[i], lst[i + 1] = lst[i + 1], lst[i]
            if i > 0:
                i -= 1
            else:
                i += 1
    return lst, lst[m]


m = randint(1, 5)
source_lst = [randint(-100, 100) for _ in range(2 * m + 1)]
print('Исходный список - ', source_lst)

print('Гномья сортировка -', dwarf_sort(source_lst[:])[0])
print('Медиана -', dwarf_sort(source_lst[:])[1])

source_lst = [randint(-100, 100) for _ in range(10)]
print('Время сортировки 10 элементов')
print(timeit('dwarf_sort(source_lst[:])', 'from __main__ import dwarf_sort, source_lst', number=1000))
source_lst = [randint(-100, 100) for _ in range(100)]
print('Время сортировки 100 элементов')
print(timeit('dwarf_sort(source_lst[:])', 'from __main__ import dwarf_sort, source_lst', number=1000))
source_lst = [randint(-100, 100) for _ in range(1000)]
print('Время сортировки 1000 элементов')
print(timeit('dwarf_sort(source_lst[:])', 'from __main__ import dwarf_sort, source_lst', number=1000))
