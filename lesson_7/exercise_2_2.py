"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.
Решите задачу тремя способами:
2) без сортировки
сделайте замеры на массивах длиной 10, 100, 1000 элементов
"""

from random import randint
from timeit import timeit


def find_m(lst):
    for i in range(len(lst) // 2):
        lst.remove(max(lst))
    return max(lst)


m = randint(1, 5)
source_lst = [randint(-100, 100) for _ in range(2 * m + 1)]
print('Исходный список - ', source_lst)

print('Медиана - ', find_m(source_lst))
source_lst = [randint(-100, 100) for _ in range(10)]
print('Время сортировки 10 элементов')
print(timeit('find_m(source_lst[:])', 'from __main__ import find_m, source_lst', number=1000))
source_lst = [randint(-100, 100) for _ in range(100)]
print('Время сортировки 100 элементов')
print(timeit('find_m(source_lst[:])', 'from __main__ import find_m, source_lst', number=1000))
source_lst = [randint(-100, 100) for _ in range(1000)]
print('Время сортировки 1000 элементов')
print(timeit('find_m(source_lst[:])', 'from __main__ import find_m, source_lst', number=1000))
