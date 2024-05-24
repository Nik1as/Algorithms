def is_perfect(num):
    return sum(i for i in range(1, num // 2 + 1) if num % i == 0) == num


if __name__ == '__main__':
    print(is_perfect(6))
    print(is_perfect(496))
    print(is_perfect(11))
