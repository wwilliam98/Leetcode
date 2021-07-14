class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        if obstacleGrid[0][0] == 1:
            return 0

        #Setup initial case, when there is rock on first col/row blocking the path, the path after the rock will all be 0
        dp[0][0] = 1
        for row in range(1, m):
            if obstacleGrid[row][0] == 0 and dp[row-1][0] == 1:
                dp[row][0] = 1
        for col in range(1, n):
            if obstacleGrid[0][col] == 0 and dp[0][col-1] == 1:
                dp[0][col] = 1

        #DP like in Unique Path
        for row in range(1, m):
            for col in range(1, n):
                if obstacleGrid[row][col] == 0:
                    dp[row][col] = dp[row-1][col] + dp[row][col-1]

        return dp[m-1][n-1]
