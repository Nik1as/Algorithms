import random


def reservoir_sampling(data, k):
    result = []
    for _ in range(k):
        result.append(data.pop(0))
    i = k
    while data:
        x = data.pop(0)
        i = i + 1
        j = random.randint(1, i)
        if j <= k:
            result[j-1] = x
    return result


if __name__ == '__main__':
    print(reservoir_sampling([1, 2, 5, 3, 6, 11, 35, 64], 3))
