class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        
        ns = len(s)
        np = len(p)
        
        pCount = collections.Counter(p)
        for i in range(ns-np+1):
            if collections.Counter(s[i:i+np]) == pCount:
                res.append(i)
        
        return res
