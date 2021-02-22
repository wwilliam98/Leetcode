class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        q = []
        m, n = len(matrix), len(matrix[0])
        visited = set()
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    visited.add((i, j))
                    q.append((i,j))
                    
        if len(q) == m*n:
            return matrix
        
        q.append((-1,-1))
        distance = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        while q:
            row, col = q.pop(0)
            if row == -1:
                distance += 1
                if q:
                    q.append((-1,-1))
                    
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                    if matrix[nr][nc] != 0:
                        matrix[nr][nc] = distance +1
                        q.append((nr, nc))
                        visited.add((nr, nc))
        
        return matrix
