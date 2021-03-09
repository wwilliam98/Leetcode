class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        self.res = []
        self.backtrack(2, n, [])
        return self.res
        
    def backtrack(self, start, n, factors):
        if len(factors) > 0:
            self.res.append(factors + [n])
        
        for i in range(start, int(math.sqrt(n))+1): #largest first pair factor is sqrt(n), ex. when n == 36, largest first pair would be 6 (6, 6). n == 16, largest first half factor would be 4
            if n % i == 0:
                self.backtrack(i, n//i, factors + [i])
