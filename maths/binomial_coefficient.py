from math import factorial


def binomial_coefficient(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))


if __name__ == '__main__':
    print(binomial_coefficient(5, 0))
    print(binomial_coefficient(6, 6))
    print(binomial_coefficient(9, 3))
