class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        r = len(obstacleGrid)
        c = len(obstacleGrid[0])
        dp = [[0 for _ in range(c)] for _ in range(r)]
        
        if obstacleGrid[0][0]:
            return 0
        
        dp[0][0] = 1
        for i in range(1, r):
            dp[i][0] = int(obstacleGrid[i][0] == 0 and obstacleGrid[i-1][0] == 0)
            if obstacleGrid[i][0] == 1:
                break
            
        for j in range(1, c):
            dp[0][j] = int(obstacleGrid[0][j] == 0 and obstacleGrid[0][j-1] == 0)
            if obstacleGrid[0][j] == 1:
                break
        
        for i in range(1, r):
            for j in range(1, c):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[r-1][c-1]
