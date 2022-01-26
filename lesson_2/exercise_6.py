"""
Задание 6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
Решите через рекурсию. Решение через цикл не принимается.
"""

from random import randint

a = randint(0, 100)


def guess_the_number(num_of_attempts):
    if num_of_attempts == 0:
        return print(f'Вы проиграли! Загаданное число - {a}')
    print(f"Осталось {num_of_attempts} попыток")
    b = input("Введите предпологаемое число: ")
    if int(b) < a:
        print('Загаданное число больше!')
        return guess_the_number(num_of_attempts - 1)
    elif int(b) > a:
        print('Загаданное число меньше!')
        return guess_the_number(num_of_attempts - 1)
    else:
        return print('Вы угадали!!!')


if __name__ == '__main__':
    guess_the_number(10)
