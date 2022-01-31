import time


def execution_time(func):
    def f(*args, **kwargs):
        start_val = time.time()
        result = func(*args, **kwargs)
        end_val = time.time()
        print("Время выполнения функции - ", end_val - start_val)
        return result

    return f


# Заполнение списка и словаря.
@execution_time
def fill_lst(lst, n):  # O(n)
    for i in range(n):  # O(n)
        lst.append(i)  # O(1)
    return


@execution_time
def fill_dct(dct, n):  # O(n)
    for i in range(n):  # O(n)
        dct[i] = i  # O(1)
    return


# Список заполняется быстрее, так как для добавления в словарь требуется вычисление хеша.

# Изменение элемента в списке и в словаре.
@execution_time
def change_el_lst(lst):
    for i in range(len(lst)):
        lst[i] = i + 1  # O(1)


@execution_time
def change_el_dct(dct):
    for i in range(len(dct)):
        dct[i] = i + 1  # O(1)


# Получение элемента в списке и в словаре.
@execution_time
def get_el_lst(lst):
    for i in range(len(lst)):
        lst[i]  # O(1)
    return


@execution_time
def get_el_dct(dct):  # O(1)
    for i in range(len(dct)):
        dct[i]  # O(1)
    return


# Удаление элемента из списка и в словаре.
@execution_time
def del_el_lst(lst):
    for i in range(len(lst)):
        lst.pop()  # O(n)
    return


@execution_time
def del_el_dct(dct):
    for i in range(len(dct)):
        del dct[i]  # O(1)
    return


print('Заполнение списка')
our_lst = []
fill_lst(our_lst, 1000000)
# Сложность O(1) для заполнения списка.
print('Измененение элемента списка')
change_el_lst(our_lst)
print('Получение элемента из списка')
get_el_lst(our_lst)
print('Удаление элемента из списка')
del_el_lst(our_lst)
# Сложность O(1) для изменения элемента списка.
# Сложность O(1) для получения элемента из списка.
# Сложность O(n) для удаления элемента из списка.

print('Заполнение словаря')
our_dct = {}
fill_dct(our_dct, 1000000)
# Сложность O(1) для заполнения словаря.
print('Измененение элемента словаря')
change_el_dct(our_dct)
print('Получение элемента из словаря')
get_el_dct(our_dct)
print('Удаление элемента из словаря')
del_el_dct(our_dct)
# Сложность O(1) для изменения элемента словаря.
# Сложность O(1) для получения элемента из словаря.
# Сложность O(1) для удаления элемента из словаря.


# Выводы:
# 1) Заполнение списка работает быстрее так как для добавления в словарь требуется вычисление хеша.
# 2) Операции изменения, получения или удаления элемента со словарем работают быстрее, так как все операции имеют
# сложность O(1), тогда как удаление элемента из списка имеет сложность O(n).
