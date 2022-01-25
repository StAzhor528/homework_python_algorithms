"""
Задание 2.
Реализуйте два алгоритма.
Оба должны обеспечивать поиск минимального значения для списка.
Сложность первого алгоритма должна быть O(n^2) - квадратичная.
Сложность второго алгоритма должна быть O(n) - линейная.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
"""


# Первая функция сложностью O(n^2).


def min_val_n2(lst):
    if len(lst) == 0:
        return 'List is empty.'
    else:
        max_diff = 0
        result = lst[0]
        for i in lst:
            for j in lst:
                diff = i - j
                if diff > 0 and diff > max_diff:
                    max_diff = diff
                    result = j
    return result


# Вторая функция сложностью O(n).


def min_val_n(lst):
    if len(lst) == 0:
        return 'List is empty.'
    result = lst[0]
    for j in lst:
        if j < result:
            result = j
    return result

if __name__ == '__main__':
    lst1 = [4, 5, 6, -872, 2, 12, 234]
    lst2 = []
    print(min_val_n2(lst1))
    print(min_val_n2(lst2))
    print(min_val_n(lst1))
    print(min_val_n(lst2))
