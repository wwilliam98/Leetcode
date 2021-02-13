class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        res = []
        d = collections.defaultdict(deque)
        for i, r in enumerate(nums):
            for j, c in enumerate(r):
                d[i+j].appendleft(c)
        
        ret = []
        for key, val in d.items():
            ret.extend(val)
        
        return ret
