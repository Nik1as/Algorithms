class Node:

    def __init__(self, data, previous=None, next=None):
        self.data = data
        self.previous = previous
        self.next = next


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        if bool(self):
            node = Node(value, self.tail)
            self.tail.next = node
            self.tail = node
        else:
            self.head = self.tail = Node(value)

    def remove(self, value):
        if bool(self):
            if self.head.data == value:
                self.head = self.head.next
                self.head.previous = None
                return
            node = self.head
            while node.next:
                if node.next.data == value:
                    tmp = node.next
                    node.next = tmp.next
                    tmp.next.previous = node
                    return
                node = node.next
        raise ValueError

    def extend(self, collection):
        for e in collection:
            self.append(e)

    def clear(self):
        self.head = None

    def __bool__(self):
        return self.head is not None

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


if __name__ == '__main__':
    a = DoublyLinkedList()
    a.append(3)
    a.append(9)
    a.append(2)
    print(a)
    a.remove(9)
    print(a)
