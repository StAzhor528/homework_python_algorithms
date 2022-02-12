"""Задача из основ Python.
Реализовать склонение слова «процент» во фразе «N процентов». Вывести эту фразу
на экран отдельной строкой для каждого из чисел в интервале от 1 до 100:
1 процент
2 процента
3 процента
4 процента
5 процентов
6 процентов
...
100 процентов"""
from memory_profiler import memory_usage


def decor(func):
    def wrapper(*args):
        m1 = memory_usage()
        res = func(args[0])
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        return res, mem_diff

    return wrapper


# Исходное решение.
@decor
def percents(lst):
    for percent in lst:
        if percent >= 11 and percent <= 19:
            print(f'{percent} процентов')
        elif percent % 10 == 1:
            print(f'{percent} процент')
        elif percent % 10 == 2 or percent % 10 == 3 or percent % 10 == 4:
            print(f'{percent} процента')
        else:
            print(f'{percent} процентов')
    return lst


res_1, mem_diff_1 = percents(list(range(1000)))


# Оптимизированное решение.
@decor
def percents(lst_1):
    for percent in lst_1:
        if percent >= 11 and percent <= 19:
            yield f'{percent} процентов'
        elif percent % 10 == 1:
            yield f'{percent} процент'
        elif percent % 10 == 2 or percent % 10 == 3 or percent % 10 == 4:
            yield f'{percent} процента'
        else:
            yield f'{percent} процентов'


if __name__ == '__main__':
    res_2, mem_diff_2 = percents(list(range(1000)))
    for i in res_2:
        print(i)
    print(f'Затраченная память исходного кода - {mem_diff_1} Mib')
    print(type(res_1))
    print(f'Затраченная память после оптимизации - {mem_diff_2} Mib')
    print(type(res_2))

# В данном примере для оптимизации воспользовался "ленивыми вычислениями". Результатом исходной функции являлся список.
# Результатом оптимизированной функции стал генератор. Так как генераторы не возвращают любое количество сразу вместе,
# а возвращают элементы один за другим, то и памяти занимают меньше.
