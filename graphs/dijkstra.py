import math
from heapq import heappop, heappush


def dijkstra(graph, s):
    n = len(graph)
    visited = [False] * n
    dist = [math.inf] * n
    dist[s] = 0
    parent = [None] * n
    heap = [(0, s)]

    while heap:
        curr_dist, min_node = heappop(heap)

        try:
            while visited[min_node]:
                curr_dist, min_node = heappop(heap)
        except IndexError:
            break

        visited[min_node] = True
        for v, weight in graph[min_node]:
            new_weight = curr_dist + weight
            if dist[v] > new_weight:
                dist[v] = new_weight
                heappush(heap, (new_weight, v))
                parent[v] = min_node
    return parent, dist


if __name__ == '__main__':
    graph = [[(1, 5), (2, 2)],
             [(3, 4), (4, 2)],
             [(1, 8), (4, 7)],
             [(4, 6), (5, 3)],
             [(5, 1)],
             []]
    print(dijkstra(graph, 0))
