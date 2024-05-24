import math


def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def farthest_insertion(coordinates):
    n = len(coordinates)
    used = [False] * n
    used[0] = True
    tour = [0]
    for _ in range(1, n):
        farthest = 0
        farthest_dist = 0
        for i in filter(lambda x: not used[x], range(n)):
            for j in tour:
                if distance(*coordinates[i], *coordinates[j]) > farthest_dist:
                    farthest = i
        used[farthest] = True

        best_index = 0
        best_tour_length = math.inf
        for i in range(len(tour)):
            new_tour = tour.copy()
            new_tour.insert(i, farthest)
            tour_length = 0
            for j in range(len(new_tour) - 1):
                tour_length += distance(*coordinates[new_tour[j]], *coordinates[new_tour[j + 1]])
            tour_length += distance(*coordinates[new_tour[-1]], *coordinates[new_tour[0]])
            if tour_length < best_tour_length:
                best_index = i
                best_tour_length = tour_length
        tour.insert(best_index, farthest)
    return tour


if __name__ == '__main__':
    coordinates = [(0, 0), (1, 1), (10, 3), (5, 1), (0, 1), (20, 5), (7, 3)]
    print(farthest_insertion(coordinates))
