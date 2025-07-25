"""
This is a bfs-version of counting-islands problem in dfs section.
Given a 2d grid map of '1's (land) and '0's (water),
count the number of islands.
An island is surrounded by water and is formed by
connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water. """


def count_islands(grid):
    row = len(grid)
    col = len(grid[0])

    num_islands = 0
    visited = [[0] * col for i in range(row)]
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    queue = []

    for i in range(row):
        for j, num in enumerate(grid[i]):
            if num == 1 and visited[i][j] != 1:
                visited[i][j] = 1
                queue.append((i, j))
                while queue:
                    x, y = queue.pop(0)
                    for k in range(len(directions)):
                        nx_x = x + directions[k][0]
                        nx_y = y + directions[k][1]
                        if nx_x >= 0 and nx_y >= 0 and nx_x < row and nx_y < col:
                            if visited[nx_x][nx_y] != 1 and grid[nx_x][nx_y] == 1:
                                queue.append((nx_x, nx_y))
                                visited[nx_x][nx_y] = 1
                num_islands += 1

    return num_islands


# Time: O(m * n)
# Space: O(m * n)


if __name__ == '__main__':
    print(count_islands([[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]))