class Node:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class SinglyLinkedList:

    def __init__(self, collection=None):
        self.head = None
        if collection:
            self.extend(collection)

    def append(self, value):
        if bool(self):
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(value)
        else:
            self.head = Node(value)

    def remove(self, value):
        if bool(self):
            if self.head.data == value:
                self.head = self.head.next
                return
            node = self.head
            while node.next:
                if node.next.data == value:
                    node.next = node.next.next
                    return
                node = node.next
        raise ValueError

    def insert(self, index, value):
        self._check_index(index)
        if index == 0 or index == -len(self):
            self.head = Node(value, self.head)
        else:
            if index < 0:
                index = len(self) + index + 1
            node = self.head
            i = 0
            while i < (index - 1):
                node = node.next
                i += 1
            node.next = Node(value, node.next)

    def index_of(self, value):
        if bool(self):
            node = self.head
            for i in enumerate(self):
                if node.data == value:
                    return i
        raise ValueError

    def extend(self, collection):
        for e in collection:
            self.append(e)

    def clear(self):
        self.head = None

    def __bool__(self):
        return not self.head is None

    def __len__(self):
        return len(tuple(iter(self)))

    def __contains__(self, item):
        for value in self:
            if value == item:
                return True
        return False

    def __add__(self, other):
        self.append(other)

    def __sub__(self, other):
        self.remove(other)

    def __iter__(self):
        node = self.head
        while node:
            yield node.data
            node = node.next

    def __str__(self):
        return f"[{', '.join([str(e) for e in self])}]"

    def _check_index(self, index):
        n = len(self)
        if n <= index < -n:
            raise ValueError


if __name__ == '__main__':
    a = SinglyLinkedList()
    a.insert(0, 4)
    a.append(4)
    a.append(35)
    a.append(8)
    a.insert(3, 0)
    a.insert(-2, 325)
    print(a)
