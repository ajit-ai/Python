import heapq
from collections import defaultdict


def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous = {node: None for node in graph}
    pq = [(0, start)]
    visited = set()

    while pq:
        dist, node = heapq.heappop(pq)
        if node in visited:
            continue
        visited.add(node)
        for neighbor, weight in graph.get(node, []):
            new_dist = dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                previous[neighbor] = node
                heapq.heappush(pq, (new_dist, neighbor))

    return distances, previous


def shortest_path(graph, start, end):
    distances, previous = dijkstra(graph, start)
    if distances[end] == float('inf'):
        return None, float('inf')
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous[current]
    return path[::-1], distances[end]


def build_graph(edges):
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    return dict(graph)
