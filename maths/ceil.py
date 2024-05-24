def ceil(x):
    return int(x) if x - int(x) <= 0 else int(x) + 1


if __name__ == '__main__':
    print(ceil(-3.2))
    print(ceil(5.3))
    print(ceil(6.7))
