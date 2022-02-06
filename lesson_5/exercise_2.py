"""
Задание 2.
Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив,
элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
Подсказка:
Попытайтесь решить это задание в двух вариантах
1) через collections
defaultdict(list)
int(, 16)
reduce
2) через ООП
вспомните про перегрузку методов
__mul__
__add__
"""

# 1) через collections
# defaultdict(list)
# int(, 16)
# reduce
from functools import reduce
from collections import defaultdict

dd = defaultdict(list)
x = input("Введите первое число в шестнадцатиричной системе: ")
y = input("Введите второе число в шестнадцатиричной системе: ")
dd[x] = list(x)
dd[y] = list(y)

sum_16 = list(hex(sum([int(''.join(v), base=16) for v in dd.values()])))
mul_16 = list(hex(reduce(lambda a, b: a * b, [int(''.join(v), base=16) for v in dd.values()])))

print("Сумма - ", sum_16[2:])
print("Произведение - ", mul_16[2:])


# 2) через ООП

class Sixteen():

    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        self.summ_16 = list(hex(int(''.join(self.x), base=16) + int(''.join(other.x), base=16)).split('0x')[-1])

    def __mul__(self, other):
        self.mul_16 = list(hex(int(''.join(self.x), base=16) * int(''.join(other.x), base=16)).split('0x')[-1])


x = ["A", "2"]
y = ["C", "4", "F"]
a = Sixteen(x)
b = Sixteen(y)
a + b
a * b
print(a.summ_16)
print(a.mul_16)
