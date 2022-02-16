"""
Задание 1.
Реализуйте кодирование строки по алгоритму Хаффмана.
У вас два пути:
1) тема идет тяжело? тогда вы можете,
опираясь на примеры с урока, сделать свою версию алгоритма
Разрешается и приветствуется изменение имен переменных,
выбор других коллекций, различные изменения
и оптимизации.
2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например,
через ООП или предложить иной подход к решению.
"""

from collections import deque, Counter


# Рекурсивная функция для реализации кортежа вида ({словарь/дерево}, вес исходной строки}), в случае длинны строки
# больше 1. Не уверен что это оптимизирует функцию, но пока разбирался с алгоритмом, решил что данное решение поможет
# лучше понять данный алгоритм. Так же этим я покажу, что не просто копировал текст задания из методички.
def rec_in_haff(tpl):
    if len(tpl) > 1:
        freq = tpl[0][1] + tpl[1][1]
        connection = {0: tpl.popleft()[0], 1: tpl.popleft()[0]}
        if len(tpl) != 0:
            for i, items in enumerate(tpl):
                if freq > items[1]:
                    continue
                else:
                    tpl.insert(i, (connection, freq))
                    break
            else:
                tpl.append((connection, freq))
            return rec_in_haff(tpl)
        else:
            tpl.append((connection, freq))
            return tpl


# Функция реализующая алгоритм Хаффмана.
# Добавил конструкцию try - except для отработки ситуации отсутствия исходной строки.
def haffman_alg(text):
    try:
        letter_dict = Counter(text)
        sort_letter = deque(sorted(letter_dict.items(), key=lambda x: x[1]))
        if len(sort_letter) > 1:
            rec_in_haff(sort_letter)
        else:
            freq = sort_letter[0][1]
            connection = {0: sort_letter.popleft()[0], 1: None}
            sort_letter.append((connection, freq))
        return sort_letter[0][0]
    except IndexError:
        print('Отсутствует элемент для кодирования!')


code_table = dict()  # Словарь следующего вида - {символ исходной строки: кодировка по Хаффману}.


# Функция заполняющая словарь-заготовку выше.
def haffman_code(binary_tree, val=''):
    if not isinstance(binary_tree, dict):
        code_table[binary_tree] = val
    else:
        haffman_code(binary_tree[0], val=f'{val}0')
        haffman_code(binary_tree[1], val=f'{val}1')


our_text = "beep boop beer!"  # Исходная строка.
our_tree = haffman_alg(our_text)  # Преобразование в бинарное дерево по Хаффману.

haffman_code(our_tree)  # Заполнение словаря {элемент строки: код}

# Вывод закодированной строки.
for el in our_text:
    print(code_table[el], end=' ')
