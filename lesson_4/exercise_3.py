"""
Задание 3.
Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.
Сделайте профилировку каждого алгоритма через timeit
Обязательно предложите еще свой вариант решения!
Сделайте вывод, какая из четырех реализаций эффективнее и почему!!!
"""
from timeit import timeit

num = 12312984719247198274154791847918274293869283749821


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(enter_num):
    lc = [el for el in str(enter_num)]
    rev_lst_lc = list(reversed(lc))
    return ''.join(rev_lst_lc)


print(timeit("revers(num)", "from __main__ import revers, num", number=10000))
print(timeit("revers_2(num)", "from __main__ import revers_2, num", number=10000))
print(timeit("revers_3(num)", "from __main__ import revers_3, num", number=10000))
print("Время выполнения моего варианта решения - ",
      timeit("revers_4(num)", "from __main__ import revers_4, num", number=10000))

# Эффективнее всего оказалась реализация через срез, так как не требует никаких дополнительных вычислений.
# Число заранее известно, а следовательно и известны индексы цифр в числе.
