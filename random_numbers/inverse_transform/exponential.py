import math
import random


def exponential(mean):
    u = random.random()
    return -mean * math.log(1 - u)


if __name__ == '__main__':
    res = [0] * 100
    n = 1_000_000

    for _ in range(n):
        x = exponential(1)
        res[int(x)] += 1
    print(list(map(lambda x: x / n, res)))
