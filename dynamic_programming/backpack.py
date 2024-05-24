def backpack(objects, G):
    n = len(objects)
    opt = [[0 for _ in range(G+1)] for _ in range(n)]

    for i in range(1, n):
        for g in range(G + 1):
            weight, value = objects[i]
            if g - value < 0:
                opt[i][g] = opt[i - 1][g]
            else:
                opt[i][g] = max(opt[i - 1][g], value + opt[i - 1][g - weight])
    return max(opt[n-1][g] for g in range(G + 1))

if __name__ == '__main__':
    objects = [(5, 3), (8, 10), (4, 2), (1, 2), (5, 10), (12, 16)]
    G = 20
    print(backpack(objects, G))