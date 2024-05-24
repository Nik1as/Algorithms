from collections import defaultdict


class MiddleSquareMethod:

    def __init__(self, seed, n):
        self.number = seed
        self.n = n

    def random(self) -> int:
        self.number = int(str(self.number * self.number).zfill(2 * self.n)[self.n - self.n // 2:self.n + self.n // 2])
        return self.number

if __name__ == '__main__':
    n = 1_000_000
    result = defaultdict(int)
    middle_square = MiddleSquareMethod(3653, 4)

    for _ in range(n):
        x = middle_square.random()
        result[x] += 1
    print(result)