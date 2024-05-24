import math
import random


def uniform(n):
    return math.floor(random.random() * n)


if __name__ == '__main__':
    outcomes = 10
    res = [0] * outcomes
    n = 1_000_000

    for _ in range(n):
        x = uniform(outcomes)
        res[x] += 1
    print(list(map(lambda x: x / n, res)))
