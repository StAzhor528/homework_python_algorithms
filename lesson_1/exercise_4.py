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

# 1-е решение. Сложность O(n) - линейная. Исходные данные - список словарей.
users_data_lst_1 = [{'login': 'aaa', 'password': 'aaa', 'activate': True},
                    {'login': 'bbb', 'password': 'bbb', 'activate': False},
                    {'login': 'ccc', 'password': 'ccc', 'activate': True}]


def autentification_1(user_login):
    user_in_lst = False
    for user_data in users_data_lst_1:  # O(n)
        if not user_in_lst:
            if user_data['login'] == user_login and user_data['activate']:
                return f'Добро пожаловать {user_login}!'
                user_in_lst = True
                break
            elif user_data['login'] == user_login and not user_data['activate']:
                print(f'Учетная запись не активирована! Пройдите аутентификацию!')
                while True:  # O(1)
                    user_password = input('Введите пароль: ')
                    if user_password == user_data['password']:
                        return f'Добро пожаловать {user_login}!'
                        user_in_lst = True
                        break
                    else:
                        print('Неверный пароль! Повторите попытку!')
                break
    if not user_in_lst:
        return f'Пользователя {user_login} не существует!'


# 2-е решение. Сложность O(1) - константная. Исходные данные - словарь.
users_data_lst_2 = {'aaa': {'password': 'aaa', 'activate': True},
                    'bbb': {'password': 'bbb', 'activate': False},
                    'ccc': {'password': 'ccc', 'activate': True}}


def autentification_2(user_login):
    if user_login in list(users_data_lst_2.keys()):  # O(1)
        if users_data_lst_2[user_login]['activate']:
            return f'Добро пожаловать {user_login}!'
        else:
            print(f'Учетная запись не активирована! Пройдите аутентификацию!')
            while True:  # O(1)
                user_password = input('Введите пароль: ')
                if user_password == users_data_lst_2[user_login]['password']:
                    return f'Добро пожаловать {user_login}!'
                    break
                else:
                    print('Неверный пароль! Повторите попытку!')
    else:
        return f'Пользователя {user_login} не существует!'

if __name__ == '__main__':
    print(autentification_1('aaa'))
    print(autentification_1('bbb'))
    print(autentification_1('ccc'))
    print(autentification_1('ddd'))

    print(autentification_2('aaa'))
    print(autentification_2('bbb'))
    print(autentification_2('ccc'))
    print(autentification_2('ddd'))
# Итог: лучше использовать 2-е решение, так как сложность наименьшая из возможных.
