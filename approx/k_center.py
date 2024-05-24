import math
import random


def k_center(points, dist, k):
    start = random.choice(points)
    c = [start]
    points.remove(start)
    for _ in range(k - 1):
        v = random.choice(points)
        for p in points:
            if min(dist(x, p) for x in c) > min(dist(x, v) for x in c):
                v = p
        c.append(v)
        points.remove(v)
    return c


if __name__ == '__main__':
    points = [(0, 1), (3, 2), (5, 1), (10, 2)]
    dist = lambda x, y: math.sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2)
    k = 2
    print(k_center(points, dist, k))
