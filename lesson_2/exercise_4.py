"""
Задание 4.	Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75
Решите через рекурсию. Решение через цикл не принимается.
Нужно обойтисть без создания массива!
"""


def sum_row(num):  # Мой изначальный вариант (тоже рабочий).
    if num == 1:  # Если число четноеб то вычитаемб если нечетное, то прибавляем.
        return num
    else:
        if num % 2 == 0:
            return sum_row(num - 1) - 1 / (2 ** (num - 1))
        return sum_row(num - 1) + 1 / (2 ** (num - 1))


def recur_method(i, numb, n_count, common_sum):  # Сделал работу над ошибками. Проработанный вариант.
    if i == n_count:
        print(f"Количество элементов - {n_count}, их сумма - {common_sum}")
    else:
        if i < n_count:
            return recur_method(i + 1, numb / 2 * - 1, n_count, common_sum + numb)


if __name__ == '__main__':
    print(sum_row(1))
    print(sum_row(2))
    print(sum_row(3))
    print(sum_row(4))
    recur_method(0, 1, 1, 0)
    recur_method(0, 1, 2, 0)
    recur_method(0, 1, 3, 0)
    recur_method(0, 1, 4, 0)
