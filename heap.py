class Heap:
    """ Класс реализующий max кучу"""
    def __init__(self):
        self.ls_main = list()

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
            self.heapify()

        return mx

    def heapify(self):
        heap_size = len(self.ls_main)
        i = 0
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
