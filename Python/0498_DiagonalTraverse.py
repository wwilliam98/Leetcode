class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        d = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i + j not in d:	#They are on the same diagonal if the sum of index are the same
                    d[i+j] = [matrix[i][j]]
                else:
                    d[i+j].append(matrix[i][j])
        
        ans = []
        for sums, arr in d.items():
            if sums % 2 == 0:
                ans += arr[::-1]
            else:
                ans += arr
        
        return ans
