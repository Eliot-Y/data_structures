class Heap:
    """ Класс реализующий max кучу"""

    def __init__(self):
        self.ls_main = list()

    def heap(ls: list):  # преобразование листа в кучу  O(n)
        heap_ls = Heap()
        heap_ls.ls_main = ls
        for i in range(len(heap_ls.ls_main) // 2, -1, -1):
            heap_ls.heapify(i)

        return heap_ls

    def add_el(self, item):
        self.ls_main.append(item)

        i = len(self.ls_main) - 1
        parent = (i - 1) // 2
        while i > 0 and self.ls_main[parent] < self.ls_main[i]:
            self.ls_main[parent], self.ls_main[i] = self.ls_main[i], self.ls_main[parent]
            i = parent
            parent = (i - 1) // 2

    def get_max(self):
        if len(self.ls_main) == 0:
            print('Извлечение из пустой кучи  ', end='')
            return False

        mx = self.ls_main[0]
        if len(self.ls_main) == 1:
            self.ls_main.pop()
        else:
            self.ls_main[0] = self.ls_main.pop()
            self.heapify(0)

        return mx

    def heapify(self, i):
        heap_size = len(self.ls_main)

        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            largest = i

            if left < heap_size and self.ls_main[left] > self.ls_main[largest]:
                largest = left

            if right < heap_size and self.ls_main[right] > self.ls_main[largest]:
                largest = right

            if largest == i:
                break

            self.ls_main[i], self.ls_main[largest] = self.ls_main[largest], self.ls_main[i]
            i = largest



