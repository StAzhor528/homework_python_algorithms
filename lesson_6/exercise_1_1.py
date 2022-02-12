"""Задача из основ Python.
Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. Например, число
«19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7. Внимание:
использовать только арифметические операции!
К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр
которых делится нацело на 7.
* Решить задачу под пунктом b, не создавая новый список."""

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
def cube_nums_1(lst):
    numbers_cube = []
    for number in lst:
        if number % 2 != 0:
            number = number ** 3
            numbers_cube.append(number)
    print('Список кубов нечетный чисел -', numbers_cube)
    general_sum = 0
    for number in numbers_cube:
        result = 0
        number_test = number
        while number_test:
            last_num = number_test % 10
            number_test = number_test // 10
            result += last_num
        if result % 7 == 0:
            general_sum = general_sum + number

    print('Сумма чисел из этого списка, сумма цифр которых делится на 7 =', general_sum)

    for i in range(len(numbers_cube)):  # Решение пункта b, без создания нового списка.
        numbers_cube[i] += 17

    print('Список кубов нечетных чисел плюс 17 -', numbers_cube)

    general_sum = 0
    for number in numbers_cube:
        result = 0
        number_test = number
        while number_test:
            last_num = number_test % 10
            number_test = number_test // 10
            result += last_num
        if result % 7 == 0:
            general_sum = general_sum + number
    print('Сумма чисел из нового списка, сумма цифр которых делится на 7 =', general_sum)
    return


res_1, mem_diff_1 = cube_nums_1(list(range(1000)))


# Оптимизированное решение.
@decor
def cube_nums_2(lst):
    numbers_cube = [number ** 3 for number in lst if number % 2 != 0]
    print('Список кубов нечетный чисел -', numbers_cube)
    general_sum = sum([number for number in numbers_cube if sum(map(int, list(str(number)))) % 7 == 0])
    print('Сумма чисел из этого списка, сумма цифр которых делится на 7 =', general_sum)
    numbers_cube = map(lambda x: x + 17, numbers_cube)
    print('Список кубов нечетных чисел плюс 17 -', numbers_cube)
    general_sum = sum((number for number in numbers_cube if sum(map(int, list(str(number)))) % 7 == 0))
    print('Сумма чисел из нового списка, сумма цифр которых делится на 7 =', general_sum)
    return


if __name__ == '__main__':
    res_2, mem_diff_2 = cube_nums_2(list(range(1000)))
    print(f'Затраченная память исходного кода - {mem_diff_1} Mib')
    print(f'Затраченная память после оптимизации - {mem_diff_2} Mib')

# В данном примере воспользовался функцией map. Результат - сильное уменьшение используемой памяти.
