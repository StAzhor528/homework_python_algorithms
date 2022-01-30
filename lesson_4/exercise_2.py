"""
Задание 2.
Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию
Выполнена попытка оптимизировать решение через мемоизацию.
Сделаны замеры обеих реализаций.
Сделайте аналитику, нужна ли здесь мемоизация или нет и почему?!!!
П.С. задание не такое простое, как кажется
"""

from timeit import timeit
from random import randint


def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


num_100 = randint(10000, 1000000)
print("Случайное число от 10000 до 1000000 - ", num_100)
num_1000 = randint(1000000, 10000000)
print("Случайное число от 1000000 до 10000000 - ", num_1000)
num_10000 = randint(100000000, 10000000000000)
print("Случайное число от 100000000 до 10000000000000 - ", num_10000)

print('Не оптимизированная функция recursive_reverse')
print(
    timeit(
        "recursive_reverse(num_100)",
        setup='from __main__ import recursive_reverse, num_100',
        number=10000))
print("Перевернутое число от 10000 до 1000000 - ", recursive_reverse(num_100))
print(
    timeit(
        "recursive_reverse(num_1000)",
        setup='from __main__ import recursive_reverse, num_1000',
        number=10000))
print("Перевернутое число от 1000000 до 10000000 - ", recursive_reverse(num_1000))
print(
    timeit(
        "recursive_reverse(num_10000)",
        setup='from __main__ import recursive_reverse, num_10000',
        number=10000))
print("Перевернутое число от 100000000 до 10000000000000 - ", recursive_reverse(num_10000))


def memoize(f):
    cache = {}

    def decorate(*args):

        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]

    return decorate


@memoize
def recursive_reverse_mem(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse_mem(number // 10)}'


print('Оптимизированная функция recursive_reverse_mem')
print(
    timeit(
        'recursive_reverse_mem(num_100)',
        setup='from __main__ import recursive_reverse_mem, num_100',
        number=10000))
print("Перевернутое число от 10000 до 1000000 - ", recursive_reverse_mem(num_100))
print(
    timeit(
        'recursive_reverse_mem(num_1000)',
        setup='from __main__ import recursive_reverse_mem, num_1000',
        number=10000))
print("Перевернутое число от 1000000 до 10000000 - ", recursive_reverse_mem(num_1000))
print(
    timeit(
        'recursive_reverse_mem(num_10000)',
        setup='from __main__ import recursive_reverse_mem, num_10000',
        number=10000))
print("Перевернутое число от 100000000 до 10000000000000 - ", recursive_reverse_mem(num_10000))

# Для наглядности добавил в код программы вывод исходных и полученных чисел.
# Вывод: в данной задаче мемоизация наобходима, так как без неё мы получаем неправильный ответ
# (в конец числа добавляется 0). Так же с мемоизацией время выполнения функции быстрее в 10-20 раз,
# если смотреть на получившиеся значения времени.
