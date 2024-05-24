def fib_iterative(n):
    a, b = 1, 1
    numbers = [1, 1]
    for _ in range(2, n):
        a, b = b, a + b
        numbers.append(b)
    return numbers


def fib_recurisve(n):
    return n if n <= 1 else fib_recurisve(n - 1) + fib_recurisve(n - 2)


if __name__ == '__main__':
    print(fib_iterative(20))
    print(fib_recurisve(20))
