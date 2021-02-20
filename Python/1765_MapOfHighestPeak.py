#Change height in Place
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        q = []
        nr = len(isWater)
        nc = len(isWater[0])
        visited = set()
        
        for i in range(nr):
            for j in range(nc):
                if isWater[i][j] == 1:
                    isWater[i][j] = 0
                    q.append((i,j))
                    visited.add((i,j))
                    
        directions = [(-1,0), (0,-1), (1,0), (0,1)]
        while q:
            row, col = q.pop(0)
            
            for dr, dc in directions:
                neighR, neighC = row + dr, col + dc
                if 0 <= neighR < nr and 0 <= neighC < nc and (neighR, neighC) not in visited:
                    isWater[neighR][neighC] = isWater[row][col] + 1
                    visited.add((neighR,neighC))
                    q.append((neighR, neighC))
                    
        return isWater

#Store the initial island
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        q = []
        first = []
        nr = len(isWater)
        nc = len(isWater[0])
        for i in range(nr):
            for j in range(nc):
                if isWater[i][j] == 1:
                    q.append((i,j))
                    first.append((i,j))
                    
        dist = 1
        directions = [(-1,0), (0,-1), (1,0), (0,1)]
        q.append((-1,-1))
        while q:
            row, col = q.pop(0)
            if row == -1:
                dist += 1
                if q:
                    q.append((-1,-1))
            
            for dr, dc in directions:
                neighR, neighC = row + dr, col + dc
                if 0 <= neighR < nr and 0 <= neighC < nc:
                    if isWater[neighR][neighC] == 0:
                        isWater[neighR][neighC] = dist
                        q.append((neighR, neighC))
            
        for r, c in first:
            isWater[r][c] = 0
        return isWater
