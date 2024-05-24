def encode(key, text):
    cipher = ''
    for char in text:
        if char.isupper():
            cipher += chr((ord(char) + key - 65) % 26 + 65)
        elif char.islower():
            cipher += chr((ord(char) + key - 97) % 26 + 97)
        else:
            cipher += char
    return cipher


def decode(key, text):
    return encode(-key, text)


if __name__ == '__main__':
    text = 'Hello World'
    key = 3
    print(encode(key, text))
    print(decode(key, encode(key, text)))
