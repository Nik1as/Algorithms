def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def ext_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        q = a // b
        g, s, t = ext_gcd(b, a % b)
        return g, t, s - q * t
