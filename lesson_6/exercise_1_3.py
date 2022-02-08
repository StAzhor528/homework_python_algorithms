"""Задача из основ Python.
Создать вручную список, содержащий цены на товары (10–20 товаров), например:
[57.8, 46.51, 97, ...]
Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп
(например «5 руб 04 коп»). Подумать, как из цены получить рубли и копейки, как добавить нули, если, например,
получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
Вывести цены, отсортированные по возрастанию, новый список не создавать
(доказать, что объект списка после сортировки остался тот же).
Создать новый список, содержащий те же цены, но отсортированные по убыванию.
Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?"""

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
def trans(lst):  # Функция для преобразования цен в вид <r> руб <kk> коп
    i = 0
    for price in lst:
        r = int(price)
        kk = round((price - int(price)) * 100)
        lst[i] = f'{r:02d} руб {kk:02d} коп'
        i += 1
    return lst


# prices = [45.66, 34.55, 67, 45.6, 77, 3, 3.9, 5.6, 3.89, 75, 21.65]
# print('id первоначального списка - ', id(prices))
# prices_new = sorted(prices)  # Список для цен, отсортированных по убыванию
# prices_new.sort(reverse=True)
# prices_five = prices_new[:5]  # Список цен пяти самых дорогих товаров
#
# trans(prices)  # Преобразование изначального списка в вид <r> руб <kk> коп
#
# print('Цены через запятую в одну строку')
# print(', '.join(prices))
# prices.sort()
# print('Цены отсортированные по возрастанию')
# print(', '.join(prices))
# print('id получившегося списка - ', id(prices))  # Доказательство что это тот самый список
# prices_new.sort(reverse=True)
#
# trans(prices_new)  # Преобразование убывающего списка в вид <r> руб <kk> коп
#
# print('id нового списка - ', id(prices_new))  # Доказательство что это новый список
# print('Цены отсортированные по убыванию')
# print(prices_new)
#
# print('Цены пяти самых дорогих товаров')
# print(prices_new[:5])
# print('Цены пяти самых дорогих товаров по возрастанию')
# prices_five.sort()  # Преобразование списка 5 дорогих товаров в вид <r> руб <kk> коп
# trans(prices_five)
# print(prices_five)

# Оптимизированное решение.
@decor
def f_1(lst):
    new_a = map(str, map(float, lst))
    return [f'{el.split(".")[0]} руб {el.split(".")[1]} коп' for el in new_a]


if __name__ == '__main__':
    res_1, mem_diff_1 = trans([45.66, 34.55, 67, 45.6, 77, 3, 3.9, 5.6, 3.89, 75, 21.65])
    res_2, mem_diff_2 = f_1([45.66, 34.55, 67, 45.6, 77, 3, 3.9, 5.6, 3.89, 75, 21.65])

    print(f'Затраченная память исходного кода - {mem_diff_1} Mib')
    print(f'Затраченная память после оптимизации - {mem_diff_2} Mib')

# В данном примере для оптимизации воспользовался встроенной функцией map и "списковым включением".
# Результат - небольшое уменьшение используемой памяти.
