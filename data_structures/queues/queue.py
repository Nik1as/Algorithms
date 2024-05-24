class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:

    def __init__(self):
        self.first = None
        self.last = None
        self.n = 0

    def enqueue(self, value):
        node = Node(value)
        if self.first is None:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node
        self.n += 1

    def dequeue(self):
        if self.first is None:
            raise ValueError

        node = self.first
        self.first = self.first.next
        if self.first is None:
            self.last = None
        self.n -= 1
        return node.data


    def front(self):
        if bool(self):
            return self.first.data
        raise ValueError

    def __iter__(self):
        node = self.first
        while node:
            yield node.data
            node = node.next

    def __len__(self):
        return self.n

    def __bool__(self):
        return not self.first is None

    def __str__(self):
        return f'[{", ".join(str(node) for node in self)}]'


if __name__ == '__main__':
    q = Queue()
    q.enqueue(3)
    q.enqueue(34)
    q.enqueue(356)
    print(q)
    print(q.front())

    while q:
        print(q.dequeue())
