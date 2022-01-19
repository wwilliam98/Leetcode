#O(N) Solution
class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        res = right = 0
        
        for i, e in enumerate(light, 1):
            right = max(right, light[i-1])
            if right == i:
                res += 1
        return res

#Slow Solution O(N^2)
class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        curr = [False] * len(light)
        l = [False] * len(light)
        count = 0
        
        for i in range(len(light)):
            curr[i] = True
            l[light[i]-1] = True
            if curr == l:
                count += 1
        return count
