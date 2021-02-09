class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        col = -1
        for i in range(len(matrix)):
            while col + len(matrix[i]) and matrix[i][col] > target:
                col -= 1
            if matrix[i][col] == target:
                return True
        return False
