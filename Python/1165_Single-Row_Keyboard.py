class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        d = {}
        curr = 0
        ret = 0
        
        for i, e in enumerate(keyboard):
            d[e] = i
        
        for w in word:
            ret += abs(d[w] - curr)
            curr = d[w]
        
        return ret
