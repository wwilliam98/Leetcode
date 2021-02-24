#O(m+n) approach, search space reduction
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        
        m = len(matrix)
        n = len(matrix[0])
        
        row = m-1
        col = 0
        
        while 0 <= row and col < n:
            if matrix[row][col] < target:
                col += 1
            elif matrix[row][col] > target:
                row -= 1
            else:
                return True
        return False

#O(m*n) approach
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        col = -1
        for i in range(len(matrix)):
            while col + len(matrix[i]) and matrix[i][col] > target:
                col -= 1
            if matrix[i][col] == target:
                return True
        return False
