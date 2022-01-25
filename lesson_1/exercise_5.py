"""
Задание 5. На закрепление навыков работы со стеком
Реализуйте структуру "стопка тарелок".
Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.
Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим
стеком порогового значения.
После реализации структуры, проверьте ее работу на различных сценариях.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
--реализуйте по аналогии с примером, рассмотренным на уроке
--создание нового стека можно реализовать добавлением новой пустой стопки
в массив стопок (lst = [[], [], [], [],....]) либо созданием объекта
класса-стек в самом же классе.
"""
"""Пример создания стека через ООП"""


class PlateStack:
    def __init__(self):
        self.elems = [[]]

    def show_all(self):  # список всех стеков.
        return self.elems

    def is_empty(self):  # проверка наличия хотя бы одного не пустого стека.
        flag = True
        for lst in self.elems:
            if lst != []:
                flag = False
        return flag

    def is_empty_first(self): # проверка первого стека на наличие элементов.
        return self.elems[0] == []

    def is_empty_last(self): # проверка последнего стека на наличие элементов.
        return self.elems[-1] == []

    def push_in(self, el): # Добавление элемента в последний стек. Если не вмещается, то создаем новый стек.
        if len(self.elems[-1]) == 2:
            self.elems.append([])
        self.elems[-1].append(el)

    def pop_out(self): # Удаление элемента из последнего стека. Если последний стек пустой, то его удаляем.
        if len(self.elems[-1]) == 0:
            self.elems.pop()
        return self.elems[-1].pop()

    def get_val(self): # Содержимое последнего стека.
        return self.elems[len(self.elems) - 1]

    def stack_size(self): # Общее количество стеков.
        return len(self.elems)

    def last_stack_size(self): # Размер последнего стека.
        return len(self.elems[-1])


if __name__ == '__main__':
    PS_OBJ = PlateStack()

    print(PS_OBJ.is_empty())
    print(PS_OBJ.is_empty_first())
    print(PS_OBJ.is_empty_last())
    PS_OBJ.push_in(1)
    PS_OBJ.push_in(2)

    PS_OBJ.push_in(1)
    PS_OBJ.push_in(2)

    PS_OBJ.push_in(1)
    PS_OBJ.push_in(2)
    print(PS_OBJ.show_all())
    print(PS_OBJ.pop_out())
    print(PS_OBJ.show_all())
    print(PS_OBJ.pop_out())
    print(PS_OBJ.pop_out())
    print(PS_OBJ.show_all())
