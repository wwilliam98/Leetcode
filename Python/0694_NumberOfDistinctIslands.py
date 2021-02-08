class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        self.path = ""
        distinctI = set()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.helper(grid, i, j, "o")
                    distinctI.add(self.path)
                    self.path = ""
        return len(distinctI)
        
    def helper(self, grid, i, j, direction):
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1: #if i and j in range, and element == 1. Checking if its island
            self.path += direction
            
            grid[i][j] = "X"

            self.helper(grid, i + 1, j, "r")
            self.helper(grid, i - 1, j, "l")
            self.helper(grid, i, j + 1, "u")
            self.helper(grid, i, j - 1, "d")
            
            self.path += "b" #back, to distinct path, ex. right - down - right and right - down - back - right
