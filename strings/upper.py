def upper(txt):
    return ''.join(chr(ord(char) - 32) if 'a' <= char <= 'z' else char for char in txt)


if __name__ == '__main__':
    print(upper('Hello World'))
