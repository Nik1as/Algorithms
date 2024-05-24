def is_pangram(txt):
    return len(set([char.lower() for char in txt if 'a' <= char.lower() <= 'z'])) == 26


if __name__ == '__main__':
    print(is_pangram('Vogel Quax zwickt Johnys Pferd Bim.'))
    print(is_pangram('abc'))
