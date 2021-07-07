class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        steps = [[float("inf") for _ in range(len(maze[0]))] for _ in range(len(maze))]
        steps[start[0]][start[1]] = 0
        queue = [start]

        while queue:
            x, y = queue.pop(0)

            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
                currstep = 0

                while nx >= 0 and ny >= 0 and nx < len(maze) and ny < len(maze[0]) and maze[nx][ny] == 0:
                    nx += dx
                    ny += dy
                    currstep += 1

                if steps[x][y] + currstep < steps[nx-dx][ny-dy]:
                    queue.append([nx-dx, ny-dy])
                    steps[nx-dx][ny-dy] = steps[x][y] + currstep
        if steps[destination[0]][destination[1]] == float("inf"):
            return -1
        else:
            return steps[destination[0]][destination[1]]
