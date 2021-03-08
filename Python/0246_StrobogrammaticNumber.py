class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        d = {"6":"9", "8":"8", "9":"6", "1":"1", "0":"0"}
        s = ""
        for i in num[::-1]:
            if i not in d:
                return False
            else:
                s += d[i]
        
        return s == num
