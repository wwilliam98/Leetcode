class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if len(matrix) == 0:
            return 0
        
        self.direction = [[0,-1], [-1, 0], [0, 1], [1, 0]]
        m = len(matrix)
        n = len(matrix[0])
        
        memo = [[-1 for _ in range(n)] for _ in range(m)]
        ans = 0
        for i in range(m):
            for j in range(n):
                self.dfs(matrix, i, j, memo)
                ans = max(ans, memo[i][j])
        return ans
    
    #Bottom-up Approach
    def dfs(self, matrix, i, j, memo):
        if memo[i][j] != -1:
            return memo[i][j]
        
        path_length = 0
        
        #Go to the deepest tile
        for x, y in self.direction:
            nx, ny = i+x, j+y
            if (0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]) and matrix[i][j] < matrix[nx][ny]):
                path_length = max(path_length, self.dfs(matrix, nx, ny, memo))
        
        #Add 1 as its a bottom up approach
        memo[i][j] = path_length + 1
        return path_length + 1 