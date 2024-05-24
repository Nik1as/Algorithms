def lower(txt):
    return ''.join(chr(ord(char) + 32) if 'A' <= char <= 'Z' else char for char in txt)


if __name__ == '__main__':
    print(lower('Hello World'))
