def breadth_first_search(graph, s, func=print):
    visited = [False] * len(graph)
    visited[s] = True

    queue = [s]

    while queue:
        v = queue.pop(0)
        func(v)
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

if __name__ == '__main__':
    graph = [[1,2],
             [2,3],
             [0,1],
             [1,2]]
    breadth_first_search(graph, 0)