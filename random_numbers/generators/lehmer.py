from collections import defaultdict


class Lehmer:

    def __init__(self, seed, modulus, multiplier):
        self.number = seed
        self.modulus = modulus
        self.multiplier = multiplier

    def random(self) -> int:
        self.number = (self.multiplier * self.number) % self.modulus
        return self.number

if __name__ == '__main__':
    n = 1_000_000
    result = defaultdict(int)
    middle_square = Lehmer(11, 2**16 + 1, 75)

    for _ in range(n):
        x = middle_square.random()
        result[x] += 1
    print(result)