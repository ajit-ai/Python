# Here's a simple implementation of BFS in Python using an adjacency list to represent a graph:

from collections import deque
import heapq

# BFS: Fixed the popleft() call (was missing parentheses)
def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)  # Add start to visited
    while queue:
        vertex = queue.popleft()  # Added parentheses
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return visited

# DFS: Added check for unvisited neighbors
def dfs(graph, start):
    visited = set()
    stack = [start]
    visited.add(start)  # Add start to visited
    while stack:
        vertex = stack.pop()
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
    return visited

# Dijkstra's: Looks mostly correct, added visited set for clarity
def dijkstra(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    queue = [(0, start)]
    visited = set()
    while queue:
        current_distance, current_vertex = heapq.heappop(queue)
        if current_vertex in visited:
            continue
        visited.add(current_vertex)
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    return distances

# Bellman-Ford: Added negative cycle detection
def bellman_ford(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    for _ in range(len(graph) - 1):
        for vertex in graph:
            for neighbor, weight in graph[vertex].items():
                distance = distances[vertex] + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
    # Check for negative-weight cycles
    for vertex in graph:
        for neighbor, weight in graph[vertex].items():
            if distances[vertex] + weight < distances[neighbor]:
                raise ValueError("Graph contains negative-weight cycle")
    return distances

# Prim's: Modified to return MST edges and total weight
def prim(graph, start):
    visited = set([start])
    edges = []
    total_weight = 0
    queue = [(weight, start, neighbor) for neighbor, weight in graph[start].items()]
    heapq.heapify(queue)
    while queue:
        weight, u, v = heapq.heappop(queue)
        if v in visited:
            continue
        visited.add(v)
        edges.append((u, v, weight))
        total_weight += weight
        for neighbor, weight in graph[v].items():
            if neighbor not in visited:
                heapq.heappush(queue, (weight, v, neighbor))
    return edges, total_weight

# Kruskal's: Added Union-Find data structure for cycle detection
class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True

def kruskal(graph):
    vertices = list(graph.keys())
    vertex_to_index = {v: i for i, v in enumerate(vertices)}
    uf = UnionFind(len(vertices))
    edges = []
    for vertex in graph:
        for neighbor, weight in graph[vertex].items():
            if vertex < neighbor:  # Avoid duplicate edges
                edges.append((weight, vertex, neighbor))
    edges.sort()
    mst = []
    total_weight = 0
    for weight, u, v in edges:
        if uf.union(vertex_to_index[u], vertex_to_index[v]):
            mst.append((u, v, weight))
            total_weight += weight
    return mst, total_weight

if __name__ == '__main__':
    # Graph represented as an adjacency list
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }
    
    start = 'A'
    
    print("BFS:", bfs(graph, start))
    print("DFS:", dfs(graph, start))
    print("Dijkstra's:", dijkstra(graph, start))
    print("Bellman-Ford:", bellman_ford(graph, start))
    print("Prim's (edges, total_weight):", prim(graph, start))
    print("Kruskal's (edges, total_weight):", kruskal(graph))