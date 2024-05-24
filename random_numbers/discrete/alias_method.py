import random
import math


def uniform(n):
    return math.floor(random.random() * n)


def biased_coin(p):
    return 'head' if random.random() < p else 'tail'


class Alias:

    def __init__(self, p):
        self.prob = [0] * len(p)
        self.alias = [0] * len(p)

        small = []
        large = []
        n = len(p)
        for i in range(n):
            p[i] = p[i] * n
            if p[i] < 1:
                small.append(i)
            else:
                large.append(i)
        while small and large:
            i = small.pop()
            j = large.pop()
            self.prob[i] = p[i]
            self.alias[i] = j
            p[j] = (p[j] + p[i]) - 1
            if p[j] < 1:
                small.append(j)
            else:
                large.append(j)
        while large:
            i = large.pop()
            self.prob[i] = 1
        while small:
            i = small.pop()
            self.prob[i] = 1

    def generate(self):
        i = uniform(len(self.prob))
        if biased_coin(self.prob[i]) == 'head':
            return i
        else:
            return self.alias[i]


if __name__ == '__main__':
    prob = [0.4, 0.2, 0.15, 0.15, 0.1]
    res = [0] * len(prob)
    n = 1_000_000
    alias = Alias(prob)

    for _ in range(n):
        x = alias.generate()
        res[x] += 1
    print(list(map(lambda x: x / n, res)))
