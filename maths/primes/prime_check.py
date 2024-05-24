import math


def prime_check(number):
    if 1 < number < 4:
        return True
    elif number < 2 or not number % 2:
        return False

    odd_numbers = range(3, int(math.sqrt(number) + 1), 2)
    return not any(not number % i for i in odd_numbers)


if __name__ == '__main__':
    print(prime_check(1))
    print(prime_check(2))
    print(prime_check(11))
    print(prime_check(561))
