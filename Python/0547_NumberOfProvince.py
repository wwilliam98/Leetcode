#BFS
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        d = {}
        n = len(isConnected)
        for i in range(1, n+1):
            d[i] = []
        
        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if isConnected[i][j] == 1:
                    d[i+1].append(j+1)
        
        ret = 0
        for i in range(1, n+1):
            q = [i]
            if i in d:
                ret += 1
            
            for j in q:
                if j in d:
                    q += d[j]
                    del d[j]
        
        return ret
