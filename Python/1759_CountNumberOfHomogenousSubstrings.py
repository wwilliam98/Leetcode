class Solution:
    def countHomogenous(self, s: str) -> int:
        if len(s) == 1:
            return 1
        
        res = 0
        counter = 0
        for i in range(len(s)):
            if i > 0 and s[i] == s[i-1]:
                counter += 1
            else:
                counter = 1
            res = (res + counter) % 1000000007
            
        return res
