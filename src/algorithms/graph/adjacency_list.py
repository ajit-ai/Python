from collections import deque, defaultdict


class Graph:
    def __init__(self, directed=False):
        self.adj = defaultdict(list)
        self.directed = directed

    def add_edge(self, u, v):
        self.adj[u].append(v)
        if not self.directed:
            self.adj[v].append(u)

    def vertices(self):
        return set(self.adj.keys())

    def edges(self):
        result = []
        for u in self.adj:
            for v in self.adj[u]:
                if self.directed or (u, v) not in result and (v, u) not in result:
                    result.append((u, v))
        return result
