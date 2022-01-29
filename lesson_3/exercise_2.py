"""
Программа для запроса и проверки пароля.
Для хранения хеша и соли используютс JSON файлы.
"""

from uuid import uuid4
import os.path
import hashlib
import json

if not os.path.exists('salt.json'):  # Условие для создания файла хранения соли.
    salt = uuid4().hex
    with open('salt.json', 'w', encoding='utf-8') as f:
        json.dump(salt, f)

if not os.path.exists('pswd.json'):  # Условие для создания файла хранения списка хешей.
    with open('pswd.json', 'w', encoding='utf-8') as f:
        json.dump([], f)

with open('salt.json', 'r', encoding='utf-8') as f:  # Считываем соль.
    salt = json.load(f)
    print('В базе данных хранится строка: ', salt)

pswd = input('Введите пароль: ')
hash_pswd = hashlib.sha256(salt.encode() + pswd.encode()).hexdigest()  # Преобразуем пароль с солью в хеш.

with open('pswd.json', 'r', encoding='utf-8') as f:  # Добавляем получившийся хеш в json файл со списком хешей.
    hash_lst = json.load(f)
if hash_pswd not in hash_lst:
    hash_lst.append(hash_pswd)
with open('pswd.json', 'w', encoding='utf-8') as f:
    json.dump(hash_lst, f)

pswd_check = input('Введите пароль еще раз для проверки: ')
hash_pswd_check = hashlib.sha256(salt.encode() +
                                 pswd_check.encode()).hexdigest()  # Преобразуем повторный пароль с солью в хеш.

if hash_pswd_check == hash_pswd:  # Проверка на совпадение паролей.
    print('Вы ввели правильный пароль')
else:
    print('Вы ввели неправильный пароль')
