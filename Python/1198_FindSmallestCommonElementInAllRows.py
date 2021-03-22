class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        freq = Counter()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                freq[mat[i][j]] += 1
        
        common = []
        for key in freq:
            if freq[key] == len(mat):
                common.append(key)
        return min(common) if common else -1
