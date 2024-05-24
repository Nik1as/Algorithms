import random_numbers


def gnome_sort(collection):
    pos = 0
    while pos < len(collection):
        if pos == 0 or collection[pos] >= collection[pos - 1]:
            pos += 1
        else:
            collection[pos], collection[pos - 1] = collection[pos - 1], collection[pos]
            pos -= 1
    return collection


if __name__ == '__main__':
    numbers = [random_numbers.randint(0, 10000) for _ in range(20)]
    print(gnome_sort(numbers))
