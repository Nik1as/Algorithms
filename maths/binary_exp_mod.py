def binary_exp_mod(base, exp, mod):
    r = 1
    if 1 & exp:
        r = base
    while exp:
        exp //= 2
        base = (base * base) % mod
        if exp & 1:
            r = (r * base) % mod
    return r
