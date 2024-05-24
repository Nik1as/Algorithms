def is_palindrome(txt):
    return txt == txt[::-1]


if __name__ == '__main__':
    print(is_palindrome('abc'))
    print(is_palindrome('z'))
    print(is_palindrome('anna'))
