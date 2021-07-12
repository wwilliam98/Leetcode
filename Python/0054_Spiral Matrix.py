class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = [matrix[0][0]]
        m, n = len(matrix), len(matrix[0])
        seen = [[False] * n for _ in range(m)]
        seen[0][0] = True
        queue = [[0,0]]
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        curr_direction = 0
        iteration = 0

        while queue:
            x, y = queue.pop()
            newRow = x
            newCol = y

            while 0 <= newRow + directions[curr_direction][0] < m and 0 <= newCol + directions[curr_direction][1] < n and not seen[newRow + directions[curr_direction][0]][newCol + directions[curr_direction][1]]:
                newRow += directions[curr_direction][0]
                newCol += directions[curr_direction][1]
                ans.append(matrix[newRow][newCol])
                seen[newRow][newCol] = True
                iteration += 1

            if iteration != (m*n)-1:
                queue.append([newRow, newCol])
            curr_direction = (curr_direction + 1) % 4

        return ans
