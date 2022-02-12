"""
Задание 1.
Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.
Сортировка должна быть реализована в виде функции.
Обязательно доработайте алгоритм (сделайте его умнее)!
Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение.
Обязательно сделайте замеры времени обеих реализаций и дайте ответ помогла ли
доработка и в каких случаях она будет эффективной.
Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.
"""
from random import randint
from timeit import timeit


def bubble_sort_1(lst):
    n = 1
    while n < len(lst):
        for i in range(len(lst) - n):
            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
        n += 1
    return lst


def bubble_sort_2(lst):
    n = 1
    flag = True
    while n < len(lst):
        for i in range(len(lst) - n):
            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                flag = False
        if flag:
            break
        n += 1
    return lst


source_lst_1 = [randint(-100, 100) for _ in range(10)]

print('1. Исходный неотсортированный массив - ', source_lst_1)

print('Отсортированный массив недоработанным методом - ', bubble_sort_1(source_lst_1[:]))
print('Отсортированный массив доработанным методом - ', bubble_sort_2(source_lst_1[:]))

print('Время работы алгоритма недоработанным методом.')
print('Время для сортировки 10 элементов: ')
print(timeit('bubble_sort_1(source_lst_1[:])', 'from __main__ import bubble_sort_1, source_lst_1', number=1000))
source_lst_1 = [randint(-100, 100) for _ in range(100)]
print('Время для сортировки 100 элементов: ')
print(timeit('bubble_sort_1(source_lst_1[:])', 'from __main__ import bubble_sort_1, source_lst_1', number=1000))
source_lst_1 = [randint(-100, 100) for _ in range(200)]
print('Время для сортировки 200 элементов: ')
print(timeit('bubble_sort_1(source_lst_1[:])', 'from __main__ import bubble_sort_1, source_lst_1', number=1000))

print('Время работы алгоритма доработанным методом.')
source_lst_1 = [randint(-100, 100) for _ in range(10)]
print('Время для сортировки 10 элементов: ')
print(timeit('bubble_sort_2(source_lst_1[:])', 'from __main__ import bubble_sort_2, source_lst_1', number=1000))
source_lst_1 = [randint(-100, 100) for _ in range(100)]
print('Время для сортировки 100 элементов: ')
print(timeit('bubble_sort_2(source_lst_1[:])', 'from __main__ import bubble_sort_2, source_lst_1', number=1000))
source_lst_1 = [randint(-100, 100) for _ in range(200)]
print('Время для сортировки 200 элементов: ')
print(timeit('bubble_sort_2(source_lst_1[:])', 'from __main__ import bubble_sort_2, source_lst_1', number=1000))

for _ in range(50):
    print('*', end='')
print()

source_lst_2 = [10 - i for i in range(10)]
print('2. Исходный массив, не требующий сортировки - ', source_lst_2)

print('Время работы алгоритма недоработанным методом.')
print('Время для сортировки 10 элементов: ')
print(timeit('bubble_sort_1(source_lst_2[:])', 'from __main__ import bubble_sort_1, source_lst_2', number=1000))
source_lst_2 = [10 - i for i in range(100)]
print('Время для сортировки 100 элементов: ')
print(timeit('bubble_sort_1(source_lst_2[:])', 'from __main__ import bubble_sort_1, source_lst_2', number=1000))
source_lst_2 = [10 - i for i in range(200)]
print('Время для сортировки 200 элементов: ')
print(timeit('bubble_sort_1(source_lst_2[:])', 'from __main__ import bubble_sort_1, source_lst_2', number=1000))

print('Время работы алгоритма доработанным методом.')
source_lst_2 = [10 - i for i in range(10)]
print('Время для сортировки 10 элементов: ')
print(timeit('bubble_sort_2(source_lst_2[:])', 'from __main__ import bubble_sort_2, source_lst_2', number=1000))
source_lst_2 = [10 - i for i in range(100)]
print('Время для сортировки 100 элементов: ')
print(timeit('bubble_sort_2(source_lst_2[:])', 'from __main__ import bubble_sort_2, source_lst_2', number=1000))
source_lst_2 = [10 - i for i in range(200)]
print('Время для сортировки 200 элементов: ')
print(timeit('bubble_sort_2(source_lst_2[:])', 'from __main__ import bubble_sort_2, source_lst_2', number=1000))

# Доработка помогает значительно в случае изначально отсортированных списков. Чем более отсортирован исходный список,
# тем эффективнее доработанный метод.
