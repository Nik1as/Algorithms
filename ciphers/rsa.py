from random import randint

from maths.binary_exp_mod import binary_exp_mod
from maths.primes.euclid import ext_gcd
from maths.primes.miller_rabin import miller_rabin_test


def random_prime(rbound=10 ** 100, lbound=2):
    a = randint(lbound, rbound)
    while not miller_rabin_test(a):
        a = randint(lbound, rbound)
    return a


def generate_key():
    p = random_prime()
    q = random_prime()
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 1
    while phi % e == 0:
        e = random_prime(phi)
    d = ext_gcd(e, phi)[1]
    if d > 0:
        return n, e, d
    if d < 0:
        return generate_key()


def encrypt(n, e, msg):
    return binary_exp_mod(msg, e, n)


def decrypt(n, d, msg):
    return binary_exp_mod(msg, d, n)


if __name__ == '__main__':
    n, e, d = generate_key()
    c = encrypt(n, e, 123)
    d = decrypt(n, d, c)
    print(c)
    print(d)
