def swap_case(txt):
    output = ''
    for char in txt:
        if char.isupper():
            output += char.lower()
        elif char.islower():
            output += char.upper()
        else:
            output += char

    return output


if __name__ == '__main__':
    print(swap_case('Hello World'))
