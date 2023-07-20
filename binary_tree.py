class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Tree:
    def __init__(self, var=None):
        self.root = None
        if var:
            try:
                for i in var:
                    self.append(i)
            except TypeError:
                self.append(var)

    def __find(self, node, parent, item):  # параметры: узел от которого ведется поиск, родительский узел и переменная
        # возвращает ссылку на узел, на родительский узел и флаг о том, был ли добавлен узел (True)
        if node is None:
            return None, parent, False

        if node.data == item:
            return node, parent, True

        if item < node.data:
            if node.left:
                return self.__find(node.left, node, item)

        if item > node.data:
            if node.right:
                return self.__find(node.right, node, item)

        return node, parent, False

    def append(self, item):  # добавить узел
        new_node = Node(item)
        if self.root is None:
            self.root = new_node
            return new_node

        sl, pr, flag_find = self.__find(self.root, None, new_node.data)  # поиск узла к которому добавится элемент

        if not flag_find and sl:
            if new_node.data < sl.data:
                sl.left = new_node
            else:
                sl.right = new_node

        return new_node

    def show_tree(self, node=-1):  # отобразить дерево в глубину (по возрастанию)
        if node == -1:
            node = self.root

        if not node:
            return

        self.show_tree(node.left)
        print(node.data, end=' ')
        self.show_tree(node.right)

    def show_wide_tree(self):  # отобразить дерево как по виду дерева
        if self.root is None:
            return False

        v = [self.root]

        while v:
            tmp_ls = []
            for ar in v:
                print(ar.data, end=' ')
                if ar.left:
                    tmp_ls.append(ar.left)
                if ar.right:
                    tmp_ls.append(ar.right)
            print()
            v = tmp_ls

    def __del_leaf(self, sl, pr):  # принимает указатель на сам узел и на его родителя, удаляет узел без потомков
        if pr.left == sl:
            pr.left = None
        elif pr.right == sl:
            pr.right = None

    def __del_one_child(self, sl, pr):  # удаляет узел с одним потомком
        if pr.left == sl:
            if sl.left is None:
                pr.left = sl.right
            elif sl.right is None:
                pr.left = sl.left

        elif pr.right == sl:
            if sl.left is None:
                pr.right = sl.right
            elif sl.right is None:
                pr.right = sl.left

    def del_node(self, key):  # удаление узла по значению
        sl, pr, flag_find = self.__find(self.root, None, key)

        if not flag_find:
            return None

        if sl.left is None and sl.right is None:
            self.__del_leaf(sl, pr)
        elif sl.right is None or sl.left is None:
            self.__del_one_child(sl, pr)
        else:
            min_node, min_node_parent = self.__find_min(sl.right, sl)
            sl.data = min_node.data
            self.__del_one_child(min_node, min_node_parent)

    def __find_min(self, node, parent):  # поиск узла с минимальным значением и его родителя
        if node.left is None:
            return node, parent

        return self.__find_min(node.left, node)

    def __clear_p(self, sl, pr):
        if sl.left:
            self.__clear_p(sl.left, sl)

        if sl.right:
            self.__clear_p(sl.right, sl)

        if pr is None:
            sl = pr = None
            self.root.data = None
            self.root = None
            return True

        if pr.left == sl:
            pr.left = None
        else:
            pr.right = None
        return

    def clear(self):
        self.__clear_p(self.root, None)

    def get_min(self):
        min_node = self.__find_min(self.root, None)[0]
        return min_node.data

    def __find_max(self, node):

        if node.right is None:
            return node

        return self.__find_max(node.right)

    def get_max(self):
        max_node = self.__find_max(self.root)
        return max_node.data

    def copy_tree(self):
        if self.root is None:
            return False

        new_object = Tree()
        v = [self.root]

        while v:
            tmp_ls = []
            for ar in v:
                new_object.append(ar.data)
                if ar.left:
                    tmp_ls.append(ar.left)
                if ar.right:
                    tmp_ls.append(ar.right)
            v = tmp_ls
        return new_object

    def mirror(self):
        if not self.root:
            return False

        self.__mirror_i(self.root)
        return True

    def __mirror_i(self, node):
        if node is None:
            return

        self.__mirror_i(node.left)
        self.__mirror_i(node.right)
        node.left, node.right = node.right, node.left




