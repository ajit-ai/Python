from collections import deque


def flood_fill(grid, sr, sc, new_color):
    if not grid or grid[sr][sc] == new_color:
        return grid
    rows, cols = len(grid), len(grid[0])
    old_color = grid[sr][sc]
    queue = deque([(sr, sc)])
    grid[sr][sc] = new_color
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == old_color:
                grid[nr][nc] = new_color
                queue.append((nr, nc))
    return grid


def flood_fill_dfs(grid, sr, sc, new_color):
    if not grid or grid[sr][sc] == new_color:
        return grid
    rows, cols = len(grid), len(grid[0])
    old_color = grid[sr][sc]

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if grid[r][c] != old_color:
            return
        grid[r][c] = new_color
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    dfs(sr, sc)
    return grid
