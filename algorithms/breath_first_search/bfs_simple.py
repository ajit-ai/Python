#It initializes a visited list to keep track of visited nodes and a queue with the starting node.
#It enters a loop that continues until the queue is empty.
#In each iteration, it dequeues a node (current_node) and checks if it has been visited before.
#If not visited, it prints the node, marks it as visited, and adds its unvisited neighbors to the queue.


from collections import deque


def bfs(graph, node):

    visited = []

    queue = deque([node])

    while queue:

        current_node = queue.popleft()

        if current_node not in visited:

            print(current_node, end=' ')

            visited.append(current_node)

            queue.extend(graph[current_node] - set(visited))


graph = {

    'A': set(['B', 'C']),

    'B': set(['A', 'D', 'E']),

    'C': set(['A', 'F']),

    'D': set(['B']),

    'E': set(['B', 'F']),

    'F': set(['C', 'E'])

}

# Start with node 'A'
bfs(graph, 'A')

# Output: A B C D E F