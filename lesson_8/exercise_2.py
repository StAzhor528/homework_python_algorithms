"""
Задание 2.
Доработайте пример структуры "дерево", рассмотренный на уроке.
Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии
 с требованиями для бинарного дерева). При валидации приветствуется генерация
 собственного исключения
Поработайте с оптимизированной структурой,
протестируйте на реальных данных - на клиентском коде
"""


class Error(Exception):
    pass


class SmallValueError(Error):
    pass


class BigValueError(Error):
    pass


class BinaryTree:
    def __init__(self, root_obj):
        self.root = root_obj  # корень
        self.left_child = None  # левый потомок
        self.right_child = None  # правый потомок

    # добавить левого потомка
    def insert_left(self, new_node):
        if self.left_child == None:  # если у узла нет левого потомка
            # Добавил исключение, на случай, если вставляемое значение больше корня.
            try:
                tree_obj = BinaryTree(new_node)
                if new_node > self.root:
                    raise BigValueError
                else:
                    self.left_child = tree_obj
            except BigValueError:
                print('Задаваемое значение для левого потомка больше корня!')
        # если у узла есть левый потомок
        else:
            # Добавил исключение, на случай, если вставляемое значение больше корня
            # или меньше существующего левого потомка.
            try:
                tree_obj = BinaryTree(new_node)
                if new_node > self.root:
                    raise BigValueError
                elif new_node < self.left_child.get_root_val():
                    raise SmallValueError
                else:
                    tree_obj.left_child = self.left_child
                    self.left_child = tree_obj
            except BigValueError:
                print('Задаваемое значение для левого потомка больше корня!')
            except SmallValueError:
                print('Задаваемое значение для левого потомка меньше существующего левого потомка!')

    # добавить правого потомка с теми же исключениями, что и при добавлении левого потомка. Знаки ">" заменил на ">".
    def insert_right(self, new_node):
        # если у узла нет правого потомка
        if self.right_child == None:
            try:
                tree_obj = BinaryTree(new_node)
                if new_node < self.root:
                    raise SmallValueError
                else:
                    self.right_child = tree_obj
            except SmallValueError:
                print('Задаваемое значение для правого потомка меньше корня!')

        # если у узла есть правый потомок
        else:
            try:
                tree_obj = BinaryTree(new_node)
                if new_node < self.root:
                    raise SmallValueError
                elif new_node > self.right_child.get_root_val():
                    raise BigValueError
                else:
                    tree_obj.right_child = self.right_child
                    self.right_child = tree_obj
            except SmallValueError:
                print('Задаваемое значение для правого потомка меньше корня!')
            except BigValueError:
                print('Задаваемое значение для правого потомка больше существующего правого потомка!')

    # метод доступа к правому потомку
    def get_right_child(self):
        try:
            return self.right_child
        except AttributeError:
            print('Искомого правого потомка в данном дереве не найдено!')

    # метод доступа к левому потомку
    def get_left_child(self):
        return self.left_child

    # метод установки корня
    def set_root_val(self, obj):
        self.root = obj

    # метод доступа к корню
    def get_root_val(self):
        return self.root


if __name__ == "__main__":
    # Корень бинарного дерева. Слева числа меньше корня, справа больше.
    r = BinaryTree(8)

    # Попытка вставить потомка не соответствующие условию бинарного дерева.
    r.insert_left(9)
    r.insert_right(7)

    # Проверка наличия потомков.
    print(r.get_left_child())
    print(r.get_left_child())

    # Вставка птомков соответствующих условию бинарного дерева.
    r.insert_left(6)
    r.insert_right(10)

    # Проверка наличия вставленных потомков.
    print(r.get_left_child().get_root_val())
    print(r.get_right_child().get_root_val())

    # Попытка вставить птомка несоответствующего условию бинарного дерева, при уже существующих потомках.
    r.insert_left(5)
    r.insert_right(11)

    # Проверка наличия потомков.
    print(r.get_left_child().get_root_val())
    print(r.get_right_child().get_root_val())

    # Вставка птомков соответствующих условию бинарного дерева, при уже существующих потомках.
    r.insert_left(7)
    r.insert_right(9)

    # Проверка наличия всех потомков.
    print(r.get_left_child().get_root_val())
    print(r.get_right_child().get_root_val())
    print(r.get_left_child().get_left_child().get_root_val())
    print(r.get_right_child().get_right_child().get_root_val())
