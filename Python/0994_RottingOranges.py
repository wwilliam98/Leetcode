class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = []
        freshO = 0
        nr, nc = len(grid), len(grid[0])
        
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == 2:
                    q.append((r,c))
                elif grid[r][c] == 1:
                    freshO += 1
        
        q.append((-1,-1))
        minute = -1
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        while q:
            row, col = q.pop(0)
            if row == -1:
                minute += 1
                if q: #Keep track of each iteration
                    q.append((-1,-1))
            
            else:
                for dr, dc in directions:
                    neighborRow, neighborCol = row + dr, col + dc
                    if 0 <= neighborRow < nr and 0 <= neighborCol < nc:
                        if grid[neighborRow][neighborCol] == 1:
                            q.append((neighborRow, neighborCol))
                            grid[neighborRow][neighborCol] = 2
                            freshO -= 1
        
        if freshO == 0:
            return minute
        else:
            return -1
