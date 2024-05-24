import math
import random


def gilbert_graph_matrix(n, p):
    graph = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if random.random() < p:
                graph[i][j] = 1
    return graph


def geometric_sample(p):
    if p == 0:
        return math.inf
    elif p == 1:
        return 0
    else:
        u = random.random()
        return math.ceil(math.log(1 - u, 1 - p) - 1)


def gilbert_graph_edges(n, p):
    edges = []
    k = -1
    while True:
        l = geometric_sample(p)
        k += l + 1
        if k < n * n:
            edges.append((k // n, k % n))
        else:
            return edges


if __name__ == '__main__':
    for row in gilbert_graph_matrix(10, 0.2):
        print(row)
    print()
    print(gilbert_graph_edges(5, 0.2))
