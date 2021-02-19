class Solution:
    def isArmstrong(self, N: int) -> bool:
        s, k = 0, len(str(N))
        for i in str(N):
            s += int(i) ** k
        return s == N
