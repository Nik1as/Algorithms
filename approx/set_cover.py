import random


def set_cover(sets, values):
    c = []
    covered = set()
    while covered != values:
        s = random.choice(sets)
        for x in sets:
            if len(x - covered) > len(s - covered):
                s = x
        c.append(s)
        sets.remove(s)
        covered.update(s)
    return c


if __name__ == '__main__':
    sets = [{1, 2, 3}, {2, 5, 7}, {2, 4, 5}, {1, 2}, {4, 8, 9, 10}, {6, 9}]
    values = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    print(set_cover(sets, values))
