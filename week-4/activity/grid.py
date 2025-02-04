def min_islands(grid, n, m):
    grid = [list(row) for row in grid]

    def expand_clouds():
        queue = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 'L':
                    queue.append((i, j))

        while queue:
            x, y = queue.pop(0)
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 'C':
                    grid[nx][ny] = 'L' 
                    queue.append((nx, ny))

    expand_clouds()  

    def dfs(x, y):
        stack = [(x, y)]
        while stack:
            cx, cy = stack.pop()
            grid[cx][cy] = 'W' 
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 'L':
                    stack.append((nx, ny))

    island_count = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'L':
                island_count += 1
                dfs(i, j) 

    return island_count


n, m = map(int, input().split())
grid = [input().strip() for _ in range(n)]

print(min_islands(grid, n, m))