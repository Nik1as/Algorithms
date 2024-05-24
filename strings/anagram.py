def is_anagram(first, second):
    return sorted(first.lower().replace(' ', '')) == sorted(second.lower().replace(' ', ''))


if __name__ == '__main__':
    print(is_anagram('Hello World', 'Hello there'))
    print(is_anagram('This is a string', 'Is this a string'))
