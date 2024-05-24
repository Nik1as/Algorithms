class MaxHeap:

    def __init__(self, data=None):
        if data:
            self._heapify(data)
        else:
            self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._repair_up(len(self.heap) - 1)

    def max(self):
        return self.heap[0]

    def delete_max(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        value = self.heap.pop()
        self._reapir_down(0)
        return value

    def _heapify(self, data):
        self.heap = data
        n = len(self)
        for i in reversed(range(n // 2)):
            self._reapir_down(i)

    def _repair_up(self, i):
        while i > 0 and self.heap[self._parent(i)] < self.heap[i]:
            self.heap[i], self.heap[self._parent(i)] = self.heap[self._parent(i)], self.heap[i]
            i = self._parent(i)

    def _reapir_down(self, i):
        while self._has_left_child(i):
            child = self._left(i)
            if self._has_right_child(i) and self.heap[child] < self.heap[self._right(i)]:
                child += 1
            if self.heap[i] >= self.heap[child]:
                break
            self.heap[i], self.heap[child] = self.heap[child], self.heap[i]
            i = child

    def __bool__(self):
        return len(self.heap) > 0

    def __len__(self):
        return len(self.heap)

    def _has_left_child(self, i):
        return self._left(i) < len(self.heap)

    def _has_right_child(self, i):
        return self._right(i) < len(self.heap)

    @staticmethod
    def _left(i):
        return 2 * i + 1

    @staticmethod
    def _right(i):
        return 2 * i + 2

    @staticmethod
    def _parent(i):
        return int((i - 1) / 2)


if __name__ == '__main__':
    h = MaxHeap()
    h.insert(2)
    h.insert(7)
    h.insert(1)
    h.insert(9)
    h.insert(3)

    while h:
        print(h.delete_max())
