class Queue:

    def __init__(self):
        self.input_stack = []
        self.output_stack = []

    def enqueue(self, x):
        self.input_stack.append(x)

    def dequeue(self):
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())
        return self.output_stack.pop()


if __name__ == '__main__':
    q = Queue()
    q.enqueue(3)
    q.enqueue(45)
    q.enqueue(64)
    print(q.dequeue())
    q.enqueue(5)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
