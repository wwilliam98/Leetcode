class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        path = [[0]*len(grid[0])]*len(grid)
        mr, mc = len(grid)-1, len(grid[0])-1
        for i in range(len(grid)-1, -1, -1):
            for j in range(len(grid[0])-1, -1, -1):
                if i == mr and j != mc: #For Bottom Row, add the right
                    path[i][j] = grid[i][j] + path[i][j+1]
                elif j == mc and i != mr:  #For most right col, add the bottom
                    path[i][j] = grid[i][j] + path[i+1][j]
                elif i != mr and j != mc:  #if its the middle part, add current and minimum between the right and bottom
                    path[i][j] = grid[i][j] + min(path[i+1][j], path[i][j+1])
                else: #where it ends (len(grid), len(grid[0]))
                    path[i][j] = grid[i][j]
        
        return path[0][0]
