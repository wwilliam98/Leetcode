class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if self.isPalindrome(s[i:j+1]):
                    res += 1
        return res
        
        
    def isPalindrome(self, s):
        return s == s[::-1]
