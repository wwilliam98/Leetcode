class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        a = [0] * 26
        for letter in p:
            a[ord(letter)-97] += 1
        
        res = []
        ls = len(s)
        lp = len(p)
        
        b = [0] * 26
        currLength = 0
        for i in range(ls):
            if currLength < lp:
                b[ord(s[i])-97] += 1
                currLength += 1
            else:
                b[ord(s[i-lp])-97] -= 1
                b[ord(s[i])-97] += 1
            
            if currLength == lp and a == b:
                res.append(i-lp+1)
        return res