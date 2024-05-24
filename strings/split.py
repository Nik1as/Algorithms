def split(txt, sep=' '):
    splited = []
    start = 0
    for i, char in enumerate(txt):
        if char == sep:
            splited.append(txt[start:i])
            start = i + 1
    splited.append(txt[start:])
    return splited


if __name__ == '__main__':
    print(split('Hello world. Have a nice day.', sep=' '))
