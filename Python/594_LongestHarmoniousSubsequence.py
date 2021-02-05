class Solution:
    def findLHS(self, nums: List[int]) -> int:
        d = {}
        res = 0
        
        for e in nums:
            if e not in d:
                d[e] = 1
            else:
                d[e] += 1
        
        for key in d:
            if key+1 in d:
                res = max(res, d[key]+d[key+1])
        
        return res
