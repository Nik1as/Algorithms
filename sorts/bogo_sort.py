import random_numbers


def bogo_sort(collection):
    def is_sorted():
        if len(collection) < 2:
            return True
        for i in range(len(collection) - 1):
            if collection[i] > collection[i + 1]:
                return False
        return True

    while not is_sorted():
        random_numbers.shuffle(collection)
    return collection


if __name__ == '__main__':
    numbers = [random_numbers.randint(0, 10000) for _ in range(10)]
    print(bogo_sort(numbers))
