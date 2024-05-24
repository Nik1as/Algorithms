from random_numbers import randint


def fermat_test(n, k=100):
    if n == 2:
        return True

    if n % 2 == 0:
        return False

    for i in range(k):
        a = randint(2, n - 2)

        if pow(a, n - 1, n) != 1:
            return False
    return True


if __name__ == '__main__':
    print(fermat_test(11))
    print(fermat_test(220))
    print(fermat_test(561))
