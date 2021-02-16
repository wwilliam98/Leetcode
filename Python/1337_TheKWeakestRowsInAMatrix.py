class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        res = []
        strength = []
        for row in range(len(mat)):
            count = 0
            for col in range(len(mat[row])):
                if mat[row][col] == 0:
                    break
                else:
                    count += 1
            
            strength.append([count, row])
            
        strength.sort()
        for i in range(k):
            res.append(strength[i][1])
        return res
