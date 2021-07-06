class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        visited = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]
        directions = [[0,1], [0, -1], [-1, 0], [1, 0]]
        queue = [start]
        visited[start[0]][start[1]] = True

        while queue:
            currx, curry = queue.pop(0)
            if currx == destination[0] and curry == destination[1]:
                return True

            for dirx, diry in directions:
                nx = currx + dirx
                ny = curry + diry
                #keep going until you hit the corner+1/OutOfBound
                while nx >= 0 and ny >= 0 and nx < len(maze) and ny < len(maze[0]) and maze[nx][ny] == 0:
                    nx += dirx
                    ny += diry

                #mark the visited end. [nx-dirx][ny-diry] is the location of the valid edge path
                if not visited[nx-dirx][ny-diry]:
                    queue.append([nx-dirx, ny - diry])
                    visited[nx-dirx][ny - diry] = True
        return False
        
