class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        self.res = []
        self.backtracking("", S, 0, len(S))
        return self.res
        
    def backtracking (self, temp, s, left, right):
        if len(temp) == len(s):
            self.res.append(temp)
            return
        
        for i in range(left, right):
            if s[i].isalpha():
                self.backtracking(temp + s[i].lower(), s, i+1, right)
                self.backtracking(temp + s[i].upper(), s, i+1, right)
                
            elif s[i].isnumeric():
                self.backtracking(temp + s[i], s, i+1, right)
