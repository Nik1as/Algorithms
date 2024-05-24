def is_pronic(num):
    if num == 0:
        return True
    for i in range(num):
        if i * (i + 1) == num:
            return True
    return False


if __name__ == '__main__':
    print(is_pronic(0))
    print(is_pronic(2))
    print(is_pronic(30))
    print(is_pronic(49))
