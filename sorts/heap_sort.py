import random_numbers

from data_structures.heap.min_heap import MinHeap


def heap_sort(collection):
    heap = MinHeap(collection)

    result = []
    while heap:
        result.append(heap.delete_min())
    return result


if __name__ == '__main__':
    numbers = [random_numbers.randint(0, 10000) for _ in range(20)]
    print(heap_sort(numbers))
