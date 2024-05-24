def is_armstrong(num, base=10):
    tmp = num
    digit_count = 0

    while tmp > 0:
        digit_count = digit_count + 1
        tmp = tmp // base

    total = 0
    tmp = num
    while tmp > 0:
        total = total + pow(tmp % base, digit_count)
        tmp = tmp // base
    return total == num


if __name__ == '__main__':
    print(is_armstrong(8208, base=10))
    print(is_armstrong(548834, base=10))
    print(is_armstrong(10, base=10))
