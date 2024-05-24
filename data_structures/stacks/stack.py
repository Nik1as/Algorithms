class Node:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack:

    def __init__(self):
        self.head = None
        self.n = 0

    def push(self, value):
        self.head = Node(value, self.head)
        self.n += 1

    def pop(self):
        if self.head is None:
            raise ValueError

        value = self.head.data
        self.head = self.head.next
        self.n -= 1
        return value

    def peek(self):
        if bool(self):
            return self.head.data
        raise ValueError

    def __len__(self):
        return self.n

    def __iter__(self):
        tmp = self.head
        while tmp is not None:
            yield tmp.data
            tmp = tmp.next

    def __str__(self):
        return f'[{", ".join([str(e) for e in self])}]'

    def __bool__(self):
        return not self.head is None


if __name__ == '__main__':
    s = Stack()
    s.push(3)
    print(len(s))
    s.push(4)
    s.push(45)
    s.push(45)
    print(len(s))
    print(s.peek())

    print(s)
    while s:
        print(s.pop())
