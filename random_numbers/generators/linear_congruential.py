from collections import defaultdict


class LinearCongruential :

    def __init__(self, seed, modulus, multiplier, increment):
        self.number = seed
        self.modulus = modulus
        self.multiplier = multiplier
        self.increment = increment

    def random(self) -> int:
        self.number = (self.multiplier * self.number + self.increment) % self.modulus
        return self.number

if __name__ == '__main__':
    n = 1_000_000
    result = defaultdict(int)
    middle_square = LinearCongruential(11, 2**16 + 1, 75, 74)

    for _ in range(n):
        x = middle_square.random()
        result[x] += 1
    print(result)