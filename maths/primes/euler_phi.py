from maths.primes.euclid import gcd


def phi(n):
    phi = 0
    for i in range(1, n + 1):
        if gcd(i, n) == 1:
            phi += 1
    return phi


if __name__ == '__main__':
    print(phi(1))
    print(phi(2))
    print(phi(6))
    print(phi(11))
