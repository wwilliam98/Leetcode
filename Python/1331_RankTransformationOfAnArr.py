class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        d = {}
        ret = []
        idx = 1
        for i in sorted(arr):
            if i not in d:
                d[i] = idx
                idx += 1
        
        for i in arr:
            ret.append(d[i])
        
        return ret
