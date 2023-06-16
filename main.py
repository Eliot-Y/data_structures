from linked_list import LinkedList, Node


def test_linked_list():
    obj_list = LinkedList()
    obj_list.show_list()
    for i in range(1, 11):
        obj_list.push_back(i ** 2)
    obj_list.show_list()
    print('contains -- ', obj_list.contains(8))
    print('contains -- ', obj_list.contains(9))
    print('index -- ', obj_list.index(6))
    print('index -- ', obj_list.index(5000000000))

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


if __name__ == '__main__':
    test_linked_list()
