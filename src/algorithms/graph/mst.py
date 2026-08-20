import heapq
from collections import defaultdict


def kruskal_mst(edges, num_vertices):
    parent = list(range(num_vertices))
    rank = [0] * num_vertices

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        rx, ry = find(x), find(y)
        if rx == ry:
            return False
        if rank[rx] < rank[ry]:
            rx, ry = ry, rx
        parent[ry] = rx
        if rank[rx] == rank[ry]:
            rank[rx] += 1
        return True

    edges_sorted = sorted(edges, key=lambda e: e[2])
    mst = []
    total = 0
    for u, v, w in edges_sorted:
        if union(u, v):
            mst.append((u, v, w))
            total += w
            if len(mst) == num_vertices - 1:
                break
    return mst, total


def prim_mst(graph, start=0):
    visited = set()
    mst = []
    total = 0
    pq = [(0, start, -1)]

    while pq and len(visited) < len(graph):
        weight, node, prev = heapq.heappop(pq)
        if node in visited:
            continue
        visited.add(node)
        if prev != -1:
            mst.append((prev, node, weight))
            total += weight
        for neighbor, w in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(pq, (w, neighbor, node))

    return mst, total
