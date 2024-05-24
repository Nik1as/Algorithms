import random_numbers


def stooge_sort(collection):
    def sort(i, j):
        if collection[i] > collection[j]:
            collection[i], collection[j] = collection[j], collection[j]
        if (j - i + 1) > 2:
            t = (j - i + 1) // 3
            sort(i, j - t)
            sort(i + t, j)
            sort(i, j - t)

    sort(0, len(collection) - 1)
    return collection


if __name__ == '__main__':
    numbers = [random_numbers.randint(0, 10000) for _ in range(20)]
    print(stooge_sort(numbers))
