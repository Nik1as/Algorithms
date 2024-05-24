from data_structures.union_find import Union


def kruskal(edges, n):
    edges.sort(key=lambda x: x[2])

    spanning_tree = []
    union = Union(n)

    for u, v, w in filter(lambda x: union.find(x[0]) != union.find(x[1]), edges):
        union.union(u, v)
        spanning_tree.append((u, v))

    if len(spanning_tree) == n - 1:
        return spanning_tree
    return None


if __name__ == '__main__':
    edges = [(0, 1, 4), (0, 5, 2), (1, 5, 3), (1, 2, 6), (2, 3, 3), (2, 5, 1), (3, 4, 2), (4, 5, 4)]
    n = 6
    print(kruskal(edges, n))
