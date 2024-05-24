import random


def biased_coin(p):
    return 'head' if random.random() < p else 'tail'


def discrete_with_coins(prob):
    mass = 1
    for i in range(len(prob)):
        if biased_coin(prob[i] / mass) == 'head':
            return i
        else:
            mass = mass - prob[i]


if __name__ == '__main__':
    prob = [0.4, 0.2, 0.15, 0.15, 0.1]
    res = [0] * len(prob)
    n = 1_000_000

    for _ in range(n):
        x = discrete_with_coins(prob)
        res[x] += 1
    print(list(map(lambda x: x / n, res)))
