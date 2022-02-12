"""Задача из основ Python.
Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield."""
from numpy import array
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
def odd_to_15_1(n):
    return [num for num in range(1, int(n), 2)]


# Оптимизированное решение.
@decor
def odd_to_15_2(n):
    return array([num for num in range(1, int(n), 2)])


if __name__ == '__main__':
    res_1, mem_diff_1 = odd_to_15_1(100000)
    res_2, mem_diff_2 = odd_to_15_2(100000)

    print(f'Затраченная память исходного кода - {mem_diff_1} Mib')
    print(f'Затраченная память после оптимизации - {mem_diff_2} Mib')

# В данном примере для оптимизации воспользовался библеотекой NumPy. При помощи функции array
# преобразовал исходный список.
# Результат - сильное уменьшение используемой памяти.
