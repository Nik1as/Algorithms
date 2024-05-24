def binary_search(collection, value):
    left = 0
    right = len(collection) - 1
    while left <= right:
        mid = (left + right) // 2
        if collection[mid] == value:
            return mid
        elif collection[mid] < value:
            left = mid + 1
        else:
            right = mid - 1


if __name__ == '__main__':
    print(binary_search([2, 34, 1, -2, 5], 1))
