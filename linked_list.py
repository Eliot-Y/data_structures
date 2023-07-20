class Node:
    def __init__(self, value=None):
        self.value = value
        self.next_node = None


class LinkedList:
    """класс реализующий односвязный список"""

    def __init__(self, vl=None):
        self._head = None
        self._tail = None
        self._max_size = 0
        self._size = 0

        if vl:
            if type(vl) == list:
                for c in vl:
                    self.push_back(c)
                    self._size += 1
            else:
                self.push_back(vl)

    def set_max_size(self, size):
        if size < 1:
            self._max_size = 0
            return True
        else:
            self._max_size = size
            while 0 < self._max_size < self._size:
                self.pop_front()

    def __find(self, find_indx=None, item=None):  # поиск узла и родителя по переданному индексу или значению
        if self._head is None:
            return None, None, None

        if not (find_indx is None):  # поиск по индексу
            current_node = self._head
            indx = 0
            pr = None

            if find_indx < 0:
                return self._head, None, False

            while current_node and indx <= find_indx:
                if indx == find_indx and self._tail == current_node:
                    return current_node, pr, True
                elif indx == find_indx:
                    return current_node, pr, False

                pr = current_node
                indx += 1
                current_node = current_node.next_node

            return current_node, pr, True  # если не нашли индекс, возвращается последний узел, True - последний узел

        elif not (item is None):  # поиск по значению
            pr = None
            current_node = self._head

            while current_node:
                if current_node.value == item:
                    return current_node, pr, False

                pr = current_node
                current_node = current_node.next_node

            return None, None, None  # возвращение ссылки на последний узел и None, если не нашли

    def contains(self, item):  # проверить находится ли элемент со значением в списке
        fl_1, fl_2, fl_3 = self.__find(item=item)
        if fl_1 is None:
            return False
        return True

    def index(self, find_indx):  # получить значение узла по индексу
        sl, pr, flag = self.__find(find_indx=find_indx)
        if sl is None:
            return pr.value
        return sl.value

    def __del_node(self, sl, pr):  # удаляет узел
        if sl is None:
            return False

        if pr is None:
            self._head = sl.next_node
            self._size -= 1
            return True

        pr.next_node = sl.next_node
        self._size -= 1

        if self._tail == sl:
            self._tail = pr
        return True

    def erase(self, item):  # удалить элемент списка по переданному значению
        sl, pr, flag = self.__find(item=item)
        return self.__del_node(sl, pr)

    def dell(self, find_indx: int):  # удалить по индексу
        sl, pr, flag = self.__find(find_indx=find_indx)
        return self.__del_node(sl, pr)

    def show_list(self):  # вывод листа
        if self._head is None:
            print('None')
            return None

        current_node = self._head
        while not (current_node is None):
            print(current_node.value, end=' ')
            current_node = current_node.next_node
        print()

    def push_back(self, item):  # добавить значение в конец
        if self._tail is None:
            self._tail = self._head = Node(item)
            self._size = 1
            return True

        new_node = Node(item)
        self._tail.next_node = new_node
        self._tail = new_node
        self._size += 1
        if 0 < self._max_size < self._size:
            self.pop_front()
        return True

    def __find_last(self):  # возвращает последний узел и его родителя
        if self._head is None:
            return False

        pr = None
        current_node = self._head
        while current_node.next_node:
            pr = current_node
            current_node = current_node.next_node

        return current_node, pr

    def push_front(self, item):  # добавить значение в начало
        if self._head is None:
            self._head = self._tail = Node(item)
            self._size = 1
            return True

        new_node = Node(item)
        new_node.next_node = self._head
        self._head = new_node
        self._size += 1

        if 0 < self._max_size < self._size:
            self.pop_back()
        return True

    def pop_back(self):  # удалить последнее значение в списке
        if self._tail is None:
            return None

        sl, pr = self.__find_last()
        pr.next_node = None
        self._tail = pr
        self._size -= 1

        return sl.value

    def pop_front(self):  # удалить первое значение в списке
        if self._head is None:
            return None

        res_value = self._head.value
        if self._tail == self._head:
            self._tail = None
        self._head = self._head.next_node

        self._size -= 1
        return res_value

    def insert(self, find_indx, item):  # вставить элемент по индексу
        if self._head is None or find_indx <= 0:
            self.push_front(item)
            return True

        sl, pr, flag_last = self.__find(find_indx=find_indx)
        if sl is None:
            self.push_back(item)
            return True

        new_node = Node(item)
        pr.next_node = new_node
        new_node.next_node = sl
        self._size += 1
        if flag_last:
            self._tail = sl

        if 0 < self._max_size < self._size:
            self.pop_front()

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
        self._size = 0

    def copy(self):  # копирование списка
        current_node = self._head
        new_link_obj = LinkedList()
        while not (current_node is None):
            new_link_obj.push_back(current_node.value)

            current_node = current_node.next_node
        new_link_obj._size = self._size
        return new_link_obj

    def extend(self, temp_ls):  # добавление нескольких переменных
        for vl in temp_ls:
            self.push_back(vl)
            self._size += 1

            if 0 < self._max_size < self._size:
                self.pop_front()
