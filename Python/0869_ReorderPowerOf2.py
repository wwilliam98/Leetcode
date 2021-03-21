class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        c = collections.Counter(str(N))
        for i in range(30):
            x = 2 ** i
            if collections.Counter(str(x)) == c:
                return True
        return False
