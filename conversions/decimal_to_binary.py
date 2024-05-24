def decimal_to_binary(decimal):
    negative = False

    if decimal < 0:
        negative = True
        decimal = -decimal

    binary = ''
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2

    if negative:
        binary = '-' + binary

    return binary


if __name__ == '__main__':
    print(decimal_to_binary(-7))
    print(decimal_to_binary(255))
    print(decimal_to_binary(12))
