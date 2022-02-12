"""
Задание 2. Массив размером 2m + 1, где m – натуральное число,
заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на
две равные по длине части:
в одной находятся элементы,
которые не меньше медианы,
в другой – не больше медианы.
Решите задачу тремя способами:
3) с помощью встроенной функции поиска медианы
сделайте замеры на массивах длиной 10, 100, 1000 элементов
В конце сделайте аналитику какой трех из способов оказался эффективнее
"""
from random import randint
from timeit import timeit
from statistics import median


def med(lst):
    return median(lst)


m = randint(1, 5)
source_lst = [randint(-100, 100) for _ in range(2 * m + 1)]
print('Исходный список - ', source_lst)

print('Медиана - ', med(source_lst))
source_lst = [randint(-100, 100) for _ in range(10)]
print('Время сортировки 10 элементов')
print(timeit('med(source_lst[:])', 'from __main__ import med, source_lst', number=1000))
source_lst = [randint(-100, 100) for _ in range(100)]
print('Время сортировки 100 элементов')
print(timeit('med(source_lst[:])', 'from __main__ import med, source_lst', number=1000))
source_lst = [randint(-100, 100) for _ in range(1000)]
print('Время сортировки 1000 элементов')
print(timeit('med(source_lst[:])', 'from __main__ import med, source_lst', number=1000))

# Итог: Самый быстрый способ по поиску медианы оказался при помощи встроенной функции. На втором месте при помощи
# поочередного удаления максимальных элементов списка. И самый долгий метод при помощи сортировки, я использовал Гномью.
