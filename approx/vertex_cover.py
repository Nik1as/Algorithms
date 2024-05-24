import random


def vertex_cover(edges) -> list:
    c = []
    while edges:
        u, v = random.choice(edges)
        c.append(u)
        c.append(v)
        edges = [e for e in edges if u not in e and v not in e]
    return c


if __name__ == '__main__':
    edges = [(0, 1), (0, 2), (1, 2), (1, 3), (1, 4), (1, 5)]
    print(vertex_cover(edges))
