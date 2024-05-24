import random


def bernoulli(p):
    if random.random() < p:
        return True
    return False


if __name__ == '__main__':
    res = [0, 0]
    n = 1_000_000

    for _ in range(n):
        x = bernoulli(0.2)
        res[int(x)] += 1
    print(list(map(lambda x: x / n, res)))
