def linear_search(collection, value):
    for i in range(len(collection)):
        if collection[i] == value:
            return i
    raise ValueError


if __name__ == '__main__':
    print(linear_search([2, 34, 1, -2, 5], 1))
