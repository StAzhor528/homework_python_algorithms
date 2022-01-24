"""
Задание 3.
Для этой задачи:
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях
3) оцените итоговую сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему
Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""

company_profit = {'A': 300, 'B': 200, 'C': 350, 'D': 50, 'E': 150, 'F': 250}


# 1-е решение. Общая сложность O(n * log n) - линейно-логарифмическая.
def best_3_first(comp_dict):
    x = sorted(company_profit.items(), key=lambda x: x[1], reverse=True) # O(n)
    return f'{x[0][0]} - 1-е место!\n\
{x[1][0]} - 2-е место!\n\
{x[2][0]} - 3-е место!'

# 2-е решение. Общая сложность O(n * log n) - линейно-логарифмическая.
def key_return(value):
    for k, v in company_profit.items(): #  O(n)
        if v == value:
            return k

def best_3_second(comp_dict):
    list_val = []
    for k, v in company_profit.items(): # O(n)
        list_val.append(v)
    list_val.sort(reverse=True) # O(n * log n) - сложность .sort. O(n) - сложность reverse.
    return f'{key_return(list_val[0])} - 1-е место!\n\
{key_return(list_val[1])} - 2-е место!\n\
{key_return(list_val[2])} - 3-е место!'

# 3-е решение. Общая сложность O(n^2) - квадратичная.
def sorting(comp_dict):
    lst_val = list(company_profit.values())
    stop_sort = True
    while stop_sort:
        stop_sort = False
        for i in range(len(lst_val) - 1):
            if lst_val[i] < lst_val[i + 1]:
                lst_val[i], lst_val[i + 1] = lst_val[i + 1], lst_val[i]
                stop_sort = True
    return f'{key_return(lst_val[0])} - 1-е место!\n\
{key_return(lst_val[1])} - 2-е место!\n\
{key_return(lst_val[2])} - 3-е место!'

if __name__ == '__main__':
    print(best_3_first(company_profit))
    print(best_3_second(company_profit))
    print(sorting(company_profit))
# Итог: лучше использовать 1-е или 2-е решение, так как сложность наименьшая из возможных.
