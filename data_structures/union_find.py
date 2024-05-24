class Union:

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1 for _ in range(n)]

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, u, v):
        u_root = self.find(u)
        v_root = self.find(v)

        if self.rank[u_root] > self.rank[v_root]:
            self.parent[v_root] = u_root
        else:
            self.parent[u_root] = v_root
            if self.rank[u_root] == self.rank[v_root]:
                self.rank[v_root] += 1
