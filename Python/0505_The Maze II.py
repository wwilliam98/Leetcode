#BFS Path finding
class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        steps = [[float("inf") for _ in range(len(maze[0]))] for _ in range(len(maze))]
        steps[start[0]][start[1]] = 0
        queue = [start]

        while queue:
            x, y = queue.pop(0)

            for dx, dy in directions:
                nx, ny = x, y
                currstep = 0

                while 0 <= nx+dx < len(maze) and 0 <= ny+dy < len(maze[0]) and maze[nx+dx][ny+dy] == 0:
                    nx += dx
                    ny += dy
                    currstep += 1

                if steps[x][y] + currstep < steps[nx][ny]:
                    queue.append([nx, ny])
                    steps[nx][ny] = steps[x][y] + currstep
        if steps[destination[0]][destination[1]] == float("inf"):
            return -1
        else:
            return steps[destination[0]][destination[1]]

#Dijkstra Path finding
import heapq
class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        steps = [[float("inf") for _ in range(len(maze[0]))] for _ in range(len(maze))]
        steps[start[0]][start[1]] = 0
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        PriorityQueue = [(0, start[0], start[1])]

        while PriorityQueue:
            d, x, y = PriorityQueue.pop(0)
            if x == destination[0] and y == destination[1]:
                return d

            """If you want to see how the algorithm works"""
            # for i in range(len(steps)):
            #     print(steps[i])
            # print(" ")

            for dx, dy in directions:
                nx, ny = x, y
                currstep = 0

                #loop until we find the edge/wall
                while 0 <= nx+dx < len(maze) and 0 <= ny+dy < len(maze[0]) and maze[nx+dx][ny+dy] != 1:
                    nx += dx
                    ny += dy
                    currstep += 1

                if steps[x][y] + currstep < steps[nx][ny]:
                    heapq.heappush(PriorityQueue, (steps[x][y] + currstep, nx, ny))
                    steps[nx][ny] = d + currstep

        return -1
