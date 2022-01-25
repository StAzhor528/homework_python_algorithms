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


# 1-е решение. Общая сложность O(n) - линейная.
def best_3_first(comp_dict):
    three_max_dict = {}
    our_dict = dict(comp_dict)
    for i in range(3):
        maximum = max(our_dict.items(), key=lambda x: x[1])
        del our_dict[maximum[0]]
        three_max_dict[maximum[0]] = maximum[1]
    return three_max_dict


# 2-е решение. Общая сложность O(n * log n) - линейно-логарифмическая.
def best_3_second(comp_dict):
    three_max_dict = {}
    lst_items = list(comp_dict.items())
    lst_items.sort(key=lambda i: i[1], reverse=True)
    for i in range(3):
        three_max_dict[lst_items[i][0]] = lst_items[i][1]
    return three_max_dict


# 3-е решение. Общая сложность O(n^2) - квадратичная.
def best_3_third(comp_dict):
    lst_items = list(comp_dict.items())
    for i in range(len(lst_items)):
        first_val_idx = i
        for j in range(i + 1, len(lst_items)):
            if lst_items[j][1] > lst_items[first_val_idx][1]:
                first_val_idx = j
        lst_items[i], lst_items[first_val_idx] = lst_items[first_val_idx], lst_items[i]
    return lst_items[0:3]


if __name__ == '__main__':
    print(best_3_first(company_profit))
    print(best_3_second(company_profit))
    print(best_3_third(company_profit))
# Итог: лучше использовать 1-е решение, так как сложность наименьшая из возможных.
