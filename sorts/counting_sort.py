import random_numbers


def counting_sort(collection):
    n = len(collection)
    minimum = min(collection)

    counting_length = max(collection) - minimum + 1
    counting = [0] * counting_length

    for number in collection:
        counting[number - minimum] += 1

    for i in range(1, counting_length):
        counting[i] = counting[i] + counting[i - 1]

    sorted = [0] * n
    for i in reversed(range(0, n)):
        sorted[counting[collection[i] - minimum] - 1] = collection[i]
        counting[collection[i] - minimum] -= 1
    return sorted


if __name__ == '__main__':
    numbers = [random_numbers.randint(0, 10000) for _ in range(20)]
    print(counting_sort(numbers))
