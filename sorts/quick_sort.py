import random_numbers


def quick_sort(collection):
    def partition(first, last):
        pivot = first
        for i in range(first, last):
            if collection[i] < collection[last]:
                collection[i], collection[pivot] = collection[pivot], collection[i]
                pivot += 1
        collection[pivot], collection[last] = collection[last], collection[pivot]
        return pivot

    def sort(first, last):
        if first < last:
            pivot = partition(first, last)

            sort(first, pivot - 1)
            sort(pivot + 1, last)

    sort(0, len(collection) - 1)
    return collection


if __name__ == '__main__':
    numbers = [random_numbers.randint(0, 10000) for _ in range(20)]
    print(quick_sort(numbers))
