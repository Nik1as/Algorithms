import math
import random


def geometric(p):
    if p == 0:
        return math.inf
    elif p == 1:
        return 0
    else:
        u = random.random()
        return math.ceil(math.log(1 - u, 1 - p) - 1)


if __name__ == '__main__':
    res = [0] * 100
    n = 1_000_000

    for _ in range(n):
        x = geometric(0.2)
        res[int(x)] += 1
    print(list(map(lambda x: x / n, res)))
