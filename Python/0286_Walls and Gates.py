class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        r, c = len(rooms), len(rooms[0])
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        queue = []

        #Find where the gates are located, then put it in the queue
        for i in range(r):
            for j in range(c):
                if rooms[i][j] == 0:
                    queue.append([i,j])

		#Regular BFS pattern
        while queue:
            x, y = queue.pop(0)
            for dx, dy in directions:
                nx, ny = x, y
                currDistance = 0 #Doesnt need to have currDist for this problem, but this would be helpful to solve other problem like the maze problem :)

                #Find neighbor that is not wall/another gate and add distance by 1
                if 0 <= nx + dx < r and 0 <= ny + dy < c and rooms[nx+dx][ny+dy] != (-1 or 0):
                    nx += dx
                    ny += dy
                    currDistance += 1

                #If the length from previous node + distance < what we have in the new row/col, update it
                if rooms[x][y] + currDistance < rooms[nx][ny]:
                    rooms[nx][ny] = rooms[x][y] + currDistance
                    queue.append([nx, ny])
