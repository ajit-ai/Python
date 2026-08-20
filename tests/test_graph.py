import pytest
from algorithms.graph.adjacency_list import Graph
from algorithms.graph.dfs import dfs_recursive, dfs_iterative, dfs_all
from algorithms.graph.dijkstra import dijkstra, shortest_path, build_graph
from algorithms.graph.topological_sort import topological_sort_bfs, topological_sort_dfs
from algorithms.graph.cycle_detection import (
    has_cycle_undirected, has_cycle_directed, connected_components
)
from algorithms.graph.mst import kruskal_mst, prim_mst
from algorithms.graph.flood_fill import flood_fill, flood_fill_dfs
from algorithms.graph.bellman_ford import bellman_ford


class TestGraph:
    def test_add_edge_undirected(self):
        g = Graph()
        g.add_edge(1, 2)
        assert 2 in g.adj[1]
        assert 1 in g.adj[2]

    def test_add_edge_directed(self):
        g = Graph(directed=True)
        g.add_edge(1, 2)
        assert 2 in g.adj[1]
        assert 1 not in g.adj.get(2, [])

    def test_vertices(self):
        g = Graph()
        g.add_edge(1, 2)
        g.add_edge(2, 3)
        assert g.vertices() == {1, 2, 3}

    def test_edges(self):
        g = Graph()
        g.add_edge(1, 2)
        g.add_edge(2, 3)
        edges = g.edges()
        assert (1, 2) in edges
        assert (2, 3) in edges


class TestDFS:
    def test_iterative(self):
        graph = {0: [1, 2], 1: [3], 2: [4], 3: [], 4: []}
        result = dfs_iterative(graph, 0)
        assert result[0] == 0
        assert set(result) == {0, 1, 2, 3, 4}

    def test_recursive(self):
        graph = {0: [1, 2], 1: [3], 2: [], 3: []}
        result = dfs_recursive(graph, 0)
        assert result[0] == 0
        assert len(result) == 4

    def test_disconnected(self):
        graph = {0: [1], 1: [], 2: [3], 3: []}
        components = dfs_all(graph)
        assert len(components) == 2

    def test_single_node(self):
        graph = {0: []}
        assert dfs_iterative(graph, 0) == [0]

    def test_cycle(self):
        graph = {0: [1], 1: [2], 2: [0]}
        result = dfs_iterative(graph, 0)
        assert set(result) == {0, 1, 2}


class TestDijkstra:
    def test_basic(self):
        graph = {0: [(1, 4), (2, 1)], 1: [(3, 1)], 2: [(1, 2), (3, 5)], 3: []}
        dist, prev = dijkstra(graph, 0)
        assert dist[0] == 0
        assert dist[1] == 3
        assert dist[2] == 1
        assert dist[3] == 4

    def test_shortest_path(self):
        graph = {0: [(1, 1), (2, 4)], 1: [(2, 2)], 2: []}
        path, dist = shortest_path(graph, 0, 2)
        assert path == [0, 1, 2]
        assert dist == 3

    def test_unreachable(self):
        graph = {0: [(1, 1)], 1: [], 2: []}
        path, dist = shortest_path(graph, 0, 2)
        assert path is None
        assert dist == float('inf')

    def test_build_graph(self):
        edges = [(0, 1, 5), (1, 2, 3)]
        graph = build_graph(edges)
        assert (1, 5) in graph[0]
        assert (0, 5) in graph[1]


class TestTopologicalSort:
    def test_bfs(self):
        graph = {0: [1, 2], 1: [3], 2: [3], 3: []}
        order = topological_sort_bfs(graph)
        assert order.index(0) < order.index(1)
        assert order.index(0) < order.index(2)
        assert order.index(1) < order.index(3)

    def test_dfs(self):
        graph = {0: [1, 2], 1: [3], 2: [3], 3: []}
        order = topological_sort_dfs(graph)
        assert order.index(0) < order.index(3)

    def test_linear(self):
        graph = {0: [1], 1: [2], 2: []}
        order = topological_sort_bfs(graph)
        assert order == [0, 1, 2]

    def test_cycle_returns_none(self):
        graph = {0: [1], 1: [2], 2: [0]}
        assert topological_sort_bfs(graph) is None


class TestCycleDetection:
    def test_undirected_cycle(self):
        graph = {0: [1, 2], 1: [0, 2], 2: [0, 1]}
        assert has_cycle_undirected(graph) is True

    def test_undirected_no_cycle(self):
        graph = {0: [1], 1: [0, 2], 2: [1]}
        assert has_cycle_undirected(graph) is False

    def test_directed_cycle(self):
        graph = {0: [1], 1: [2], 2: [0]}
        assert has_cycle_directed(graph) is True

    def test_directed_no_cycle(self):
        graph = {0: [1], 1: [2], 2: []}
        assert has_cycle_directed(graph) is False

    def test_connected_components(self):
        graph = {0: [1], 1: [0], 2: [3], 3: [2], 4: []}
        comps = connected_components(graph)
        assert len(comps) == 3

    def test_single_component(self):
        graph = {0: [1, 2], 1: [0, 2], 2: [0, 1]}
        comps = connected_components(graph)
        assert len(comps) == 1


class TestMST:
    def test_kruskal(self):
        edges = [(0, 1, 4), (0, 2, 3), (1, 2, 1), (1, 3, 2), (2, 3, 5)]
        mst, total = kruskal_mst(edges, 4)
        assert len(mst) == 3
        assert total == 6

    def test_prim(self):
        graph = {
            0: [(1, 4), (2, 3)],
            1: [(0, 4), (2, 1), (3, 2)],
            2: [(0, 3), (1, 1), (3, 5)],
            3: [(1, 2), (2, 5)]
        }
        mst, total = prim_mst(graph, 0)
        assert len(mst) == 3
        assert total == 6

    def test_kruskal_single(self):
        mst, total = kruskal_mst([], 1)
        assert mst == []
        assert total == 0


class TestFloodFill:
    def test_bfs(self):
        grid = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
        result = flood_fill(grid, 1, 1, 2)
        assert result == [[2, 2, 2], [2, 2, 0], [2, 0, 1]]

    def test_dfs(self):
        grid = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
        result = flood_fill_dfs(grid, 1, 1, 2)
        assert result == [[2, 2, 2], [2, 2, 0], [2, 0, 1]]

    def test_no_change(self):
        grid = [[1, 2], [2, 1]]
        result = flood_fill(grid, 0, 0, 1)
        assert result == [[1, 2], [2, 1]]

    def test_fill_all(self):
        grid = [[0, 0], [0, 0]]
        result = flood_fill(grid, 0, 0, 3)
        assert result == [[3, 3], [3, 3]]

    def test_single_cell(self):
        grid = [[1]]
        result = flood_fill(grid, 0, 0, 5)
        assert result == [[5]]


class TestBellmanFord:
    def test_basic(self):
        edges = [(0, 1, 4), (0, 2, 5), (1, 2, -2), (2, 3, 3)]
        dist = bellman_ford(edges, 4, 0)
        assert dist[0] == 0
        assert dist[1] == 4
        assert dist[2] == 2
        assert dist[3] == 5

    def test_negative_cycle(self):
        edges = [(0, 1, 1), (1, 2, -1), (2, 0, -1)]
        assert bellman_ford(edges, 3, 0) is None

    def test_single_node(self):
        dist = bellman_ford([], 1, 0)
        assert dist == [0]

    def test_unreachable(self):
        edges = [(0, 1, 1)]
        dist = bellman_ford(edges, 3, 0)
        assert dist[2] == float('inf')
