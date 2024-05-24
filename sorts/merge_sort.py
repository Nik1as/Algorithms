import random_numbers


def merge_sort(collection):
    def merge(a, b):
        c = []
        while len(a) != 0 and len(b) != 0:
            if a[0] < b[0]:
                c.append(a[0])
                a.remove(a[0])
            else:
                c.append(b[0])
                b.remove(b[0])
        if len(a) == 0:
            c += b
        else:
            c += a
        return c

    if len(collection) < 2:
        return collection
    else:
        middle = len(collection) // 2
        a = merge_sort(collection[:middle])
        b = merge_sort(collection[middle:])
        return merge(a, b)


if __name__ == '__main__':
    numbers = [random_numbers.randint(0, 10000) for _ in range(20)]
    print(merge_sort(numbers))
