class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        res = []
        s = defaultdict()
        changed.sort()
        
        for e in changed:
            if e in s and s[e] > 0:
                res.append(e//2)
                s[e] -= 1
            else:
                if e*2 not in s:
                    s[e*2] = 1
                else:
                    s[e*2] += 1
                
        for i, e in s.items():
            if e != 0:
                return []
        return res