class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        previous = [[0] * (len(B) + 1) for _ in range(len(A) + 1)] #
        for i in range(len(A) - 1, -1, -1):
            for j in range(len(B) - 1, -1, -1):
                if A[i] == B[j]:
                    previous[i][j] = previous[i + 1][j + 1] + 1 #From the last max_length, add 1
        return max(max(row) for row in previous) #return the maximum number in the arr(previous)
