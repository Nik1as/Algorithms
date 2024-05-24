import random_numbers


def selection_sort(collection):
    length = len(collection)
    for i in range(length - 1):
        least = i
        for k in range(i + 1, length):
            if collection[k] < collection[least]:
                least = k
        if least != i:
            collection[least], collection[i] = collection[i], collection[least]
    return collection


if __name__ == '__main__':
    numbers = [random_numbers.randint(0, 10000) for _ in range(20)]
    print(selection_sort(numbers))
