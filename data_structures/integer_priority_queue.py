class IntegerPriorityQueue:

    def __init__(self, n):
        self.n = n
        self.data = [[] for _ in range(n)]

    def push(self, value, prio):
        self.data[prio].append(value)

    def pop(self):
        for i in range(self.n - 1, -1, -1):
            if self.data[i]:
                return self.data[i].pop()


if __name__ == '__main__':
    q = IntegerPriorityQueue(5)
    q.push(10, 2)
    q.push(5, 3)
    q.push(8, 4)

    for _ in range(3):
        print(q.pop())
