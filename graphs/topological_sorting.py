def topological_sorting(graph):
    n = len(graph)
    in_degree = [0] * n
    for i in range(n):
        for v in graph[i]:
            in_degree[v] += 1

    stack = []
    for i in range(n):
        if in_degree[i] == 0:
            stack.append(i)

    result = []
    while stack:
        i = stack.pop()
        result.append(i)

        for v in graph[i]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                stack.append(v)
    if len(result) == n:
        return result
    raise ValueError


if __name__ == '__main__':
    graph = [[],
             [],
             [3],
             [1],
             [0, 1],
             [0, 2]]
    print(topological_sorting(graph))
