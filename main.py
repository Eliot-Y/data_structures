from linked_list import LinkedList, Node
from binary_tree import Tree, Node


def test_linked_list():
    obj_list = LinkedList()
    obj_list.show_list()
    for i in range(1, 11):
        obj_list.push_back(i ** 2)
    obj_list.show_list()
    print('contains -- ', obj_list.contains(8))
    print('contains -- ', obj_list.contains(9))
    print('index 6 -- ', obj_list.index(6))
    print('index 5000 -- ', obj_list.index(5000000000))

    obj_list.dell(5)
    obj_list.push_back(12345)
    obj_list.push_front(555)
    obj_list.push_front(111)
    obj_list.push_front(999)
    obj_list.show_list()
    for i in range(5):
        obj_list.pop_front()
        obj_list.pop_back()
    obj_list.show_list()
    obj_list.erase(9)
    obj_list.erase(16)
    obj_list.show_list()

    print('\nCreate object 2')
    obj2 = LinkedList(12, 24, 53, 90)
    obj2.insert(2, 404)
    obj2.extend('098765')
    obj2.extend(4, 3, 2, 1)
    obj2.show_list()

    obj3 = obj2.copy()
    for _ in range(8):
        obj3.pop_back()
    obj2.show_list()
    obj3.show_list()
    obj3.clear()
    obj3.show_list()


def test_binary_tree():
    obt = Tree()

    ls = [10, 5, 7, 16, 13, 2, 20]
    for x in ls:
        obt.append(x)

    obt.show_wide_tree()
    obt.del_node(20)

    for x in range(2, 15, 2):
        obt.append(x)
    obt.show_wide_tree()
    print()
    obt.show_tree()
    print(f"\nmax = {obt.get_max()}\nmin = {obt.get_min()}")
    obt2 = obt.copy_tree()
    obt2.show_wide_tree()
    print(f'hash obt  {hash(obt)}\nhash obt2 {hash(obt2)}')


if __name__ == '__main__':
    # test_linked_list()
    test_binary_tree()
