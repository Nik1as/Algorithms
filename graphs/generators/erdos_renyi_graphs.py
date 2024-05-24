import others.reservoir_sampling


def erdos_renyi_graph(n, m):
    edges = []
    for i in range(n):
        for j in range(n):
            edges.append((i, j))

    return others.reservoir_sampling.reservoir_sampling(edges, m)


if __name__ == '__main__':
    print(erdos_renyi_graph(5, 10))
