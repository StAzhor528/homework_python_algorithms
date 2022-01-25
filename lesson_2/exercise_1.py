"""
Задание 1.	Написать программу, которая будет складывать, вычитать,
умножать или делить два числа. Числа и знак операции вводятся пользователем.
После выполнения вычисления программа не должна завершаться, а должна
запрашивать новые данные для вычислений. Завершение программы должно
выполняться при вводе символа '0' в качестве знака операции. Если пользователь
вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна
сообщать ему об ошибке и снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.
Подсказка:
Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, / - ШАГ РЕКУРСИИ
- условие завершения рекурсии - введена операция 0 - БАЗОВЫЙ СЛУЧАЙ
Решите через рекурсию. Решение через цикл не принимается.
Пример:
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 214
Введите второе число: 234
Ваш результат 448
Введите операцию (+, -, *, / или 0 для выхода): -
Введите первое число: вп
Вы вместо трехзначного числа ввели строку (((. Исправьтесь
Введите операцию (+, -, *, / или 0 для выхода):
"""


def math_operation():
    sign = input("Введите операцию (+, -, *, / или 0 для выхода): ")
    if sign == '0':
        return
    elif sign in ['+', '-', '*', '/']:
        first_num = input("Введите первое число: ")
        if not first_num.isdigit():
            print("Вы вместо числа ввели строку (((. Исправьтесь!")
            return math_operation()
        second_num = input("Введите второе число: ")
        if not second_num.isdigit():
            print("Вы вместо числа ввели строку (((. Исправьтесь!")
            return math_operation()
        if sign == '+':
            result = int(first_num) + int(second_num)
            print(f'Ваш результат {result}')
            return math_operation()
        if sign == '-':
            result = int(first_num) - int(second_num)
            print(f'Ваш результат {result}')
            return math_operation()
        if sign == '*':
            result = int(first_num) * int(second_num)
            print(f'Ваш результат {result}')
            return math_operation()
        if sign == '/':
            if int(second_num) == 0:
                print('Нельзя делить на ноль! Повторите ввод!')
                return math_operation()
            else:
                result = int(first_num) / int(second_num)
                print(f'Ваш результат {result}')
                return math_operation()
    else:
        print('Неверный ввод! Попробуйте еще раз!')
        return math_operation()


if __name__ == '__main__':
    math_operation()
