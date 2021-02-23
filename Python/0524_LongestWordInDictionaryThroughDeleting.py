class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        res = ""
        for string in d:
            if self.isSubstring(string, s):
                if len(string) > len(res) or (len(string) == len(res) and string < res):
                    res = string
        return res
        
        
    def isSubstring(self, subS, s1):
        i = 0
        for s in s1:
            if s == subS[i]:
                i += 1
                if i == len(subS):
                    return True
        return False
