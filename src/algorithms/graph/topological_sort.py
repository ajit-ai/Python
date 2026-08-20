from collections import defaultdict, deque


def topological_sort_bfs(graph):
    in_degree = defaultdict(int)
    nodes = set()
    for u in graph:
        nodes.add(u)
        for v, _ in graph[u] if graph[u] and isinstance(graph[u][0], tuple) else [(v, None) for v in graph[u]]:
            nodes.add(v)
            in_degree[v] += 1
    for node in nodes:
        if node not in in_degree:
            in_degree[node] = 0

    queue = deque([n for n in nodes if in_degree[n] == 0])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for v, _ in graph.get(node, []) if graph.get(node) and isinstance(graph[node][0], tuple) else [(v, None) for v in graph.get(node, [])]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    if len(order) != len(nodes):
        return None
    return order


def topological_sort_dfs(graph):
    visited = set()
    order = []
    nodes = set()
    for u in graph:
        nodes.add(u)
        for v, _ in graph[u] if graph[u] and isinstance(graph[u][0], tuple) else [(v, None) for v in graph[u]]:
            nodes.add(v)

    def dfs(node):
        visited.add(node)
        for v, _ in graph.get(node, []) if graph.get(node) and isinstance(graph[node][0], tuple) else [(v, None) for v in graph.get(node, [])]:
            if v not in visited:
                dfs(v)
        order.append(node)

    for node in nodes:
        if node not in visited:
            dfs(node)

    result = order[::-1]
    node_set = set()
    for n in result:
        if n in node_set:
            return None
        node_set.add(n)
    return result
