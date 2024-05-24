def factorial_iterative(n):
    value = 1
    for i in range(1, n + 1):
        value *= i
    return value


def factorial_recursive(n):
    return 1 if n == 0 or n == 1 else n * factorial_recursive(n - 1)


if __name__ == '__main__':
    print(factorial_iterative(4))
    print(factorial_recursive(4))
