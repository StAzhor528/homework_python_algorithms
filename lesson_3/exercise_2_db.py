"""
Решение 2го задания через db-api.
Данный код писал с разбора ДЗ, параллельно читая статью на хабре про db-api.
С кодом разобрался.
"""

import hashlib
from sqlite3 import connect, OperationalError, IntegrityError
import os.path


class HashClass:
    def __init__(self):
        self.db_obj = os.path.join(os.path.dirname(__file__), "demo.sqlite")
        self.conn = connect(self.db_obj)
        self.crs = self.conn.cursor()

    def create_tbl(self):

        create_stmt = "CREATE TABLE user_info (user_login varchar(255) unique, user_password varchar(255)"
        try:
            self.crs.execute(create_stmt)
        except OperationalError:
            print("Таблица уже существует.")
        else:
            self.conn.commit()
            print("Таблица добавлена в БД")

    @staticmethod
    def get_hash():
        login = input("Введите логин: ")
        pswd = input("Введите пароль: ")
        hash_pswd = hashlib.sha256(login.encode() + pswd.encode()).hexdigest()
        return login, hash_pswd

    def register(self):
        login, reg_hash = self.get_hash()
        insert_stmt = "INSERT INTO user_info (user_login, user_password) VALUES (?, ?)"
        user_info = (login, reg_hash)
        try:
            self.crs.execute(insert_stmt, user_info)
        except IntegrityError:
            print("Вы уже зарегистрированы")
        else:
            self.conn.commit()
            print("Вы успешно зарегистрированы")

    def log_in(self):
        login, check_hash = self.get_hash()
        select_stmt = "SELECT user_password FROM user_info WHERE user_login = ?"
        self.crs.execute(select_stmt, login)
        out_hash = self.crs.fetchone()
        if check_hash == out_hash[0]:
            print("Добро пожаловать!")
        else:
            print("Введен неверный пароль или вы не зарегистрировались!")


network = HashClass()
network.create_tbl()
network.register()
network.log_in()
