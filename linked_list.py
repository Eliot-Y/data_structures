class Node:
    def __init__(self, value=None):
        self.value = value
        self.next_node = None


class LinkedList:
    """класс реализующий односвязный список"""

    def __init__(self, *args):
        self._head = None
        self._tail = None
        if len(args) > 0:
            self.extend(args)

    def contains(self, item):  # проверить находится ли узел в списке
        current_node = self._head
        while not (current_node is None):
            if item == current_node.value:
                return True
            else:
                current_node = current_node.next_node
        return False

    def index(self, find_indx):  # получить значение узла по индексу
        current_node = self._head
        indx = 0
        while not (current_node is None) and 0 <= indx <= find_indx:
            if indx == find_indx:
                return current_node.value
            indx += 1
            current_node = current_node.next_node
        return None

    def erase(self, item):  # удалить элемент списка по переданному значению
        if self._head is None:
            return False

        current_node = self._head
        while not (current_node is None) and 0 <= item:
            if current_node.value == item:
                if self._head == current_node:
                    self.pop_front()
                    return True
                if self._tail == current_node:
                    self.pop_back()
                    return True
                left.next_node = current_node.next_node
                del current_node
                return True

            left = current_node
            current_node = current_node.next_node
        return False

    def dell(self, find_indx: int):  # удалить по индексу
        if find_indx == 0:
            self.pop_front()
            return True

        current_node = self._head
        indx = 0
        while not (current_node is None) and 0 <= indx <= find_indx:
            if indx == find_indx:
                left_node.next_node = current_node.next_node

                if current_node.next_node is None:
                    self._tail = left_node
                del current_node
                return True

            left_node = current_node
            current_node = current_node.next_node
            indx += 1
        return None

    def show_list(self):  # вывод листа
        current_node = self._head
        if current_node is None:
            print('None')
            return None
        while not (current_node is None):
            print(current_node.value, end=' ')
            current_node = current_node.next_node
        print()

    def push_back(self, item):  # добавить значение в конец
        if self._tail is None:
            self._tail = self._head = Node(item)
            return True

        new_node = Node(item)
        self._tail.next_node = new_node
        self._tail = new_node
        return True

    def push_front(self, item):  # добавить значение в начало
        if self._head is None:
            self._head = self._tail = Node(item)
            return True
        new_node = Node(item)
        new_node.next_node = self._head
        self._head = new_node
        return True

    def pop_back(self):  # удалить последнее значение в списке
        res_value = None
        if self._tail is None:
            return None

        current_node = self._head
        while not (current_node.next_node is None):
            left = current_node
            current_node = current_node.next_node
        left.next_node = None
        self._tail = left
        res_value = current_node.value
        del current_node
        return res_value

    def pop_front(self):  # удалить первое значение в списке
        res_value = None
        if self._head is None:
            return None

        ptr = self._head
        res_value = self._head.value
        if self._tail == self._head:
            self._tail = None
        self._head = self._head.next_node

        del ptr
        return res_value

    def insert(self, find_indx, item):  # вставить элемент по индексу
        if self._head is None or find_indx <= 0:
            self.push_front(item)
            return True
        current_node = self._head
        indx = 0
        while not (current_node is None):
            if current_node.next_node is None:
                self.push_back(item)
                return True

            if indx == find_indx:
                new_node = Node(item)
                left.next_node = new_node
                new_node.next_node = current_node
                return True

            left = current_node
            indx += 1
            current_node = current_node.next_node
        self.push_back(item)
        return True

    def clear(self):  # очистить список
        current_node = self._head
        while not (current_node is None):
            left = current_node
            current_node = current_node.next_node
            left.next_node = None
            left.value = None
        self._tail = None
        self._head = None

    def copy(self):  # копирование списка
        current_node = self._head
        new_link_obj = LinkedList()
        while not (current_node is None):
            new_link_obj.push_back(current_node.value)

            current_node = current_node.next_node
        return new_link_obj

    def extend(self, temp_ls, *args):  # добавление нескольких переменных
        try:
            for vl in temp_ls:
                self.push_back(vl)
        except:
            self.push_back(temp_ls)

        for vl in args:
            self.push_back(vl)


