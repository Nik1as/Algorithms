def collatz(n):
    sequence = [n]
    while n != 1:
        n = 3 * n + 1 if n & 1 else n // 2
        sequence.append(n)
    return sequence


if __name__ == '__main__':
    print(collatz(7))
