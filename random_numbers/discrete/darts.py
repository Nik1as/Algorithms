import random
import math


def uniform(n):
    return math.floor(random.random() * n)


def biased_coin(p):
    return 'head' if random.random() < p else 'tail'


class Darts:

    def __init__(self, p):
        self.p = p
        self.p_max = max(p)

    def generate(self):
        while True:
            i = uniform(len(self.p))
            if biased_coin(self.p[i] / self.p_max) == 'head':
                return i


if __name__ == '__main__':
    prob = [0.4, 0.2, 0.15, 0.15, 0.1]
    res = [0] * len(prob)
    n = 1_000_000
    alias = Darts(prob)

    for _ in range(n):
        x = alias.generate()
        res[x] += 1
    print(list(map(lambda x: x / n, res)))
