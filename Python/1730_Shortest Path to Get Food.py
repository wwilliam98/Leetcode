class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        steps = [[math.inf for _ in range(n)] for _ in range(m)]
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        queue = []

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "*":
                    steps[i][j] = 0
                    queue.append([i, j])

        while queue:
            x, y = queue.pop(0)
            if grid[x][y] == "#":
                return steps[x][y]

            for dx, dy in directions:
                nx, ny = x, y

                if 0 <= nx + dx < m and 0 <= ny + dy < n and grid[nx + dx][ny + dy] != "X":
                    nx += dx
                    ny += dy

                    if steps[x][y] + 1 < steps[nx][ny]:
                        steps[nx][ny] = steps[x][y] + 1
                        queue.append([nx, ny])
        return -1
