class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        if not grid:
            return True
        
        self.directions = {1: [(0, -1), (0, 1)],
                           2: [(-1, 0), (1, 0)],
                           3: [(0, -1), (1, 0)],
                           4: [(0, 1), (1, 0)],
                           5: [(0, -1), (-1, 0)],
                           6: [(-1, 0), (0, 1)]}
        
        self.visited = set()
        return self.dfs(grid, 0, 0)
        
    def dfs(self, grid, r, c):
        self.visited.add((r,c))
        if r == len(grid)-1 and c == len(grid[0])-1:
            return True
        
        for dr, dc in self.directions[grid[r][c]]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and (nr, nc) not in self.visited and (-dr, -dc) in self.directions[grid[nr][nc]]:
                if self.dfs(grid, nr, nc):
                    return True
        
        return False
