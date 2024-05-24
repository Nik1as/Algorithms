import math


def floyd_warshal(edges, n):
    dist = [[math.inf for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for u, v, w in edges:
        dist[u][v] = w

    for r in range(n):
        for u in range(n):
            for v in range(n):
                dist[u][v] = min(dist[u][v], dist[u][r] + dist[r][v])
    return dist


if __name__ == '__main__':
    edges = [(0, 1, 3), (0, 3, 5), (1, 0, 2), (1, 3, 4), (2, 1, 1), (3, 2, 2)]
    print(floyd_warshal(edges, 4))
