def power(x, y):
    if y < 0:
        return 1 / power(x, -y)
    if y == 0:
        return 1
    tmp = power(x, int(y / 2))
    if y % 2 == 0:
        return tmp * tmp
    else:
        return x * tmp * tmp


if __name__ == '__main__':
    print(power(2, 8))
    print(power(6, 3))
    print(power(3, 0))
    print(power(-3, 2))
    print(power(3, -2))
