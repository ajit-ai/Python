from collections import deque


def dfs_recursive(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    result = [start]
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            result.extend(dfs_recursive(graph, neighbor, visited))
    return result


def dfs_iterative(graph, start):
    visited = set()
    result = []
    stack = [start]
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        result.append(node)
        for neighbor in reversed(graph.get(node, [])):
            if neighbor not in visited:
                stack.append(neighbor)
    return result


def dfs_all(graph):
    visited = set()
    result = []
    for node in graph:
        if node not in visited:
            component = dfs_recursive(graph, node, visited)
            result.append(component)
    return result
