class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        res = []
        last = {}
        for i, c in enumerate(S):
            last[c] = i
        
        j = lastPartitionIndex = 0
        for i,c in enumerate(S):
            j = max(j, last[c])
            if i == j:
                res.append(i-lastPartitionIndex+1)
                lastPartitionIndex = j + 1
        
        return res
