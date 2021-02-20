class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        res = 0
        d = {}
        
        for i in dominoes:
            p = tuple(sorted(i))
            if p in d:
                d[p] += 1
            else:
                d[p] = 1
        
        c = 0
        for n in d.values():
            s = n*(n-1) // 2 #Formula of sum from 1 to (n-1), n*(n+1) // 2 sum from 1 to n
            c += s
        return c
