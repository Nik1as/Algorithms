def floor(x):
    return int(x) if x - int(x) >= 0 else int(x) - 1


if __name__ == '__main__':
    print(floor(-3.2))
    print(floor(5.3))
    print(floor(6.7))
