def depth_first_search(graph, s, func=print):
    def search(v, visited):
        visited[v] = True
        func(v)
        for i in graph[v]:
            if not visited[i]:
                search(i, visited)

    visited = [False] * len(graph)
    search(s, visited)

if __name__ == '__main__':
    graph = [[1, 2],
             [2, 3],
             [0, 1],
             [1, 2]]
    depth_first_search(graph, 0)