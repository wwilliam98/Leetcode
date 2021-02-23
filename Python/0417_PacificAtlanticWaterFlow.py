#Without For Loop
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []
        
        res = []
        r, c = len(matrix), len(matrix[0])
        self.pacific = [[False for _ in range(c)] for _ in range(r)]  #not the same as [[False]*c]*r
        self.atlantic = [[False for _ in range(c)] for _ in range(r)] #not the same as [[False]*c]*r
        
        for i in range(r):
            self.dfs(matrix, self.pacific, 0, i, 0)
            self.dfs(matrix, self.atlantic, 0, i, c-1)
        
        for j in range(c):
            self.dfs(matrix, self.pacific, 0, 0, j)
            self.dfs(matrix, self.atlantic, 0, r-1, j)
        
        for i in range(r):
            for j in range(c):
                if self.pacific[i][j] and self.atlantic[i][j]:
                    res.append([i, j])
        
        return res
        
    def dfs(self, grid, visited, prev, i, j):
        if i < 0 or len(grid) <= i or j < 0 or len(grid[0]) <= j or visited[i][j] or grid[i][j] < prev:
            return
        visited[i][j] = True
        self.dfs(grid, visited, grid[i][j], i + 1, j)
        self.dfs(grid, visited, grid[i][j], i - 1, j)
        self.dfs(grid, visited, grid[i][j], i, j + 1)
        self.dfs(grid, visited, grid[i][j], i, j - 1)

#Using For Loop
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []
        ret = []
        r, c = len(matrix), len(matrix[0])
        self.pacific = [[False for _ in range(c)] for _ in range(r)]  #not the same as [[False]*c]*r
        self.atlantic = [[False for _ in range(c)] for _ in range(r)] #not the same as [[False]*c]*r
        self.directions = [(1,0),(-1,0),(0,1),(0,-1)]
        
        for i in range(r):
            self.dfs(matrix, self.pacific, i, 0)
            self.dfs(matrix, self.atlantic, i, c-1)
        
        for j in range(c):
            self.dfs(matrix, self.pacific, 0, j)
            self.dfs(matrix, self.atlantic, r-1, j)
        
        for i in range(r):
            for j in range(c):
                if self.pacific[i][j] and self.atlantic[i][j]:
                    ret.append([i,j])
        return ret
        
    def dfs(self, grid, visited, i, j):
        visited[i][j] = True
        
        for dr, dc in self.directions:
            nr, nc = i + dr, j + dc
            if nr < 0 or len(grid) <= nr or nc < 0 or len(grid[0]) <= nc or visited[nr][nc] or grid[i][j] > grid[nr][nc]:
                continue
            self.dfs(grid, visited, nr, nc)
