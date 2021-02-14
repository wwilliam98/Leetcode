#Shorter Solution same idea
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        if grid[0][0] or grid[n-1][n-1]:
            return -1
        
        q = [(0, 0)]
        grid[0][0] = 1
        
        while q:
            i, j = q.pop(0)
            if i == n-1 and j == n-1: 
                return grid[i][j]
            
            for x, y in ((i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)):
                if 0 <= x < n and 0 <= y < n and not grid[x][y]:
                    grid[x][y] = grid[i][j]+1
                    q.append((x, y))
        return -1

#Longer solution, but more understandable
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        mrow = len(grid)-1
        mcol = len(grid[0])-1
        
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        
        def neighbor(row, col):
            for r, c in directions:
                newR = row + r
                newC = col + c
                if newR < 0 or newR > mrow or newC < 0 or newC > mcol or grid[newR][newC] != 0:
                    continue
                
                yield(newR, newC)
             
        if grid[0][0] != 0 or grid[mrow][mcol] != 0:
            return -1
        
        q = [(0,0)]
        grid[0][0] = 1
        
        while q:
            row, col = q.pop(0)
            distance = grid[row][col]
            if col == mcol and row == mrow:
                return distance
            
            for nrow, ncol in neighbor(row, col):
                grid[nrow][ncol] = distance + 1
                q.append((nrow, ncol))
            
        return -1
