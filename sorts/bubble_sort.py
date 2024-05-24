import random_numbers


def bubble_sort(collection):
    length = len(collection)
    for i in range(length - 1):
        swapped = False
        for j in range(length - i - 1):
            if collection[j] > collection[j + 1]:
                collection[j], collection[j + 1] = collection[j + 1], collection[j]
                swapped = True
        if not swapped:
            break
    return collection


if __name__ == '__main__':
    numbers = [random_numbers.randint(0, 10000) for _ in range(20)]
    print(bubble_sort(numbers))
