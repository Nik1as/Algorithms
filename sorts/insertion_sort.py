import random_numbers


def insertion_sort(collection):
    for i in range(len(collection)):
        cursor = collection[i]
        pos = i

        while pos > 0 and collection[pos - 1] > cursor:
            collection[pos] = collection[pos - 1]
            pos -= 1
        collection[pos] = cursor
    return collection


if __name__ == '__main__':
    numbers = [random_numbers.randint(0, 10000) for _ in range(20)]
    print(insertion_sort(numbers))
