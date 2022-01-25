"""
Задание 4.
Для этой задачи:
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему
Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.
Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.
Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""


# 1-е решение. Сложность O(n) - линейная.

def autentification_1(users, name, password):
    for k, v in users.items():
        if k == name:
            if v['password'] == password and v['activate']:
                return f'Добро пожаловать {name}!'
            elif v['password'] == password and not v['activate']:
                return 'Учетная запись не активирована! Пройдите аутентификацию!'
            elif v['password'] != password:
                return 'Неверный пароль!'
    return f'Пользователя {name} не существует!'


# 2-е решение. Сложность O(n) - константная. Исходные данные - словарь.


def autentification_2(users, name, password):
    if users.get(name):
        if users[name]['password'] == password and users[name]['activate']:
            return f'Добро пожаловать {name}!'
        elif users[name]['password'] == password and not users[name]['activate']:
            return 'Учетная запись не активирована! Пройдите аутентификацию!'
        elif users[name]['password'] != password:
            return 'Неверный пароль!'
    else:
        return f'Пользователя {name} не существует!'


if __name__ == '__main__':
    users_data_lst = {'aaa': {'password': 'aaa', 'activate': True},
                      'bbb': {'password': 'bbb', 'activate': False},
                      'ccc': {'password': 'ccc', 'activate': True}}

    print(autentification_1(users_data_lst, 'aaa', 'aaa'))
    print(autentification_1(users_data_lst, 'bbb', 'bbb'))
    print(autentification_1(users_data_lst, 'ccc', 'fff'))
    print(autentification_1(users_data_lst, 'ddd', 'ddd'))

    print(autentification_2(users_data_lst, 'aaa', 'aaa'))
    print(autentification_2(users_data_lst, 'bbb', 'bbb'))
    print(autentification_2(users_data_lst, 'ccc', 'fff'))
    print(autentification_2(users_data_lst, 'ddd', 'ddd'))
# Итог: лучше использовать 2-е решение, так как сложность наименьшая из возможных.
