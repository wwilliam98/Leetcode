class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        q = [] #most BFS will always need queue, while loop, and for loop
        r, c = len(grid), len(grid[0])
        
        for i in range(r): #Search for something we need (in this case island)
            for j in range(c):
                if grid[i][j] == 1:
                    q.append((i, j))
                    
        if not q or len(q) == r * c: #base case if its all Island / Water
            return -1
        
        q.append((-1,-1)) #To mark down/flag every iteration (doesnt have to be -1)
        distance = -1
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        while q: 
            row, col = q.pop(0)
            if row == -1: #If we found marker/flag, add to iteration (in this case distance)
                distance += 1
                if q: #At some point, the iteration will end. if not end yet, we want to keep mark it down
                    q.append((-1,-1))
            
            for dr, dc in directions: #(dr: direction row, dc: direction column)
                nr, nc = row + dr, col + dc #get the neighbors
                if 0 <= nr < r and 0 <= nc < c: #if its inbound / in matrix
                    if grid[nr][nc] == 0:
                        grid[nr][nc] = "Visited" #mark the visited neighbor and put it in queue
                        q.append((nr, nc))  
        
        return distance
