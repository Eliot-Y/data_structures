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

    def __find(self, find_indx=None, item=None):  # поиск узла и родителя по переданному индексу или значению
        if self._head is None:
            return None, None

        if not (find_indx is None):
            current_node = self._head
            indx = 0
            pr = None

            if indx < 0:
                return self._head, None

            while current_node.next_node and indx <= find_indx:
                if indx == find_indx:
                    return current_node, pr

                pr = current_node
                indx += 1
                current_node = current_node.next_node

            return current_node, pr  # если не нашли индекс, возвращается последний узел

        elif not (item is None):
            pr = None
            current_node = self._head

            while current_node:
                if current_node.value == item:
                    return current_node, pr

                pr = current_node
                current_node = current_node.next_node

            return None, None  # возвращение ссылки на последний узел и None, если не нашли

    def contains(self, item):  # проверить находится ли узел в списке
        fl_1, fl_2 = self.__find(item=item)
        if fl_1 is None:
            return False
        return True

    def index(self, find_indx):  # получить значение узла по индексу
        sl, pr = self.__find(find_indx=find_indx)
        return sl.value

    def __del_node(self, sl, pr):  # удаляет узел
        if sl is None:
            return False

        if pr is None:
            self._head = sl.next_node
            return True

        pr.next_node = sl.next_node

        if self._tail == sl:
            self._tail = pr
        return True

    def erase(self, item):  # удалить элемент списка по переданному значению
        sl, pr = self.__find(item=item)
        return self.__del_node(sl, pr)

    def dell(self, find_indx: int):  # удалить по индексу
        sl, pr = self.__find(find_indx=find_indx)
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
            return True

        new_node = Node(item)
        self._tail.next_node = new_node
        self._tail = new_node
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
            return True

        new_node = Node(item)
        new_node.next_node = self._head
        self._head = new_node
        return True

    def pop_back(self):  # удалить последнее значение в списке
        if self._tail is None:
            return None

        sl, pr = self.__find_last()
        pr.next_node = None
        self._tail = pr

        return sl.value

    def pop_front(self):  # удалить первое значение в списке
        if self._head is None:
            return None

        res_value = self._head.value
        if self._tail == self._head:
            self._tail = None
        self._head = self._head.next_node

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


ob = LinkedList()
for x in range(11):
    ob.push_back(x*2)

ob.show_list()
ob.insert(10, 11111)
ob.show_list()

