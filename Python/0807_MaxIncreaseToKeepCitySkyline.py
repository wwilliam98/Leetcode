class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        ret = 0
        leftview = []
        topview = []
        
        for i in range(len(grid)):
            leftview.append(max(grid[i]))
            topview.append(self.findmaxincol(grid, i))
        
        for i in range(len(leftview)):
            for j in range(len(topview)):
                mini = min(leftview[i], topview[j])
                ret += mini - grid[i][j]
        return ret
        
    def findmaxincol(self, grid, col):
        m = -1
        for r in range(len(grid)):
            m = max(m, grid[r][col])
        return m
