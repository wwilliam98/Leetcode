import heapq
class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        visited[0][0] = True

        directions = [[0,1], [1,0], [0,-1], [-1,0]]
        queue = [(-grid[0][0], 0, 0)]
        while queue:
            val, x, y = heapq.heappop(queue)
            print(queue, val, x, y)
            if x == m-1 and y == n-1:
                return -val

            for dx, dy in directions:
                nx, ny = x, y
                if 0 <= nx + dx < m and 0 <= ny + dy < n and not visited[nx+dx][ny+dy]:
                    nx += dx
                    ny += dy
                    visited[nx][ny] = True
                    heapq.heappush(queue, (max(val, -grid[nx][ny]), nx, ny))
