def binary_to_decimal(binary):
    binary = str(binary).strip()

    if not binary:
        raise ValueError

    negative = binary[0] == '-'
    if negative:
        binary = binary[1:]

    if not all(char in '01' for char in binary):
        raise ValueError

    decimal = 0
    for char in binary:
        decimal = 2 * decimal + int(char)
    return -decimal if negative else decimal


if __name__ == '__main__':
    print(binary_to_decimal('1111'))
    print(binary_to_decimal('00000'))
    print(binary_to_decimal('1010'))
