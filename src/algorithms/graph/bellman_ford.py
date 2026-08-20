def bellman_ford(edges, num_vertices, start):
    dist = [float('inf')] * num_vertices
    dist[start] = 0

    for _ in range(num_vertices - 1):
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    for u, v, w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            return None

    return dist
