class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[1] * n for _ in range(n)]
        matrix[0][0] = 1

        seen = [[False] * n for _ in range(n)]
        seen[0][0] = True

        queue = [[0,0]]
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        curr_direction = 0
        iteration = 1

        while queue:
            x, y = queue.pop()
            newRow = x
            newCol = y

            while 0 <= newRow + directions[curr_direction][0] < n and 0 <= newCol + directions[curr_direction][1] < n and not seen[newRow + directions[curr_direction][0]][newCol + directions[curr_direction][1]]:
                newRow += directions[curr_direction][0]
                newCol += directions[curr_direction][1]
                matrix[newRow][newCol] = iteration + 1
                seen[newRow][newCol] = True
                iteration += 1

            if iteration != (n*n):
                queue.append([newRow, newCol])
            curr_direction = (curr_direction + 1) % 4

        ans = []
        for r in range(n):
            ans.append(matrix[r])
        return ans
