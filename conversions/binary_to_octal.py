def binary_to_octal(binary):
    binary = str(binary).strip()

    if not binary:
        raise ValueError

    negative = binary[0] == '-'
    if negative:
        binary = binary[1:]

    if not all(char in '01' for char in binary):
        raise ValueError

    octal = ''
    n = len(binary)
    binary = binary.zfill(n + 3 - (n % 3))

    while binary:
        value = 0
        for char in binary[:3]:
            value = 2 * value + int(char)
        octal += str(value)
        binary = binary[3:]

    return '-' + octal if negative else octal


if __name__ == '__main__':
    if __name__ == '__main__':
        print(binary_to_octal('1111'))
        print(binary_to_octal('00000'))
        print(binary_to_octal('-1010'))
