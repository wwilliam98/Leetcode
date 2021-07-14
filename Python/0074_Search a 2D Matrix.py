class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        if m == 0:
            return False

        left, right = 0, m*n-1
        while left <= right:
            mid = (left + right) // 2
            element = matrix[mid // n][mid % n]
            if target == element:
                return True

            if target < element:
                right = mid - 1
            else:
                left = mid + 1
        return False
