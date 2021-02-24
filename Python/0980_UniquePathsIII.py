class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.ret = 0
        steps = 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    x, y = (i, j)
                    
                elif grid[i][j] == 0:
                    steps += 1
        
        self.dfs(grid, x, y, steps)
        return self.ret
        
    def dfs(self, grid, i, j, steps):
        if i < 0 or len(grid) <= i or j < 0 or len(grid[i]) <= j or grid[i][j] < 0:
            return
        
        if grid[i][j] == 2:
            if steps == 0:
                self.ret += 1
            return
        
        grid[i][j] = -1
        self.dfs(grid, i, j + 1, steps-1)
        self.dfs(grid, i, j - 1, steps-1)
        self.dfs(grid, i + 1, j, steps-1)
        self.dfs(grid, i - 1, j, steps-1)
        grid[i][j] = 0
