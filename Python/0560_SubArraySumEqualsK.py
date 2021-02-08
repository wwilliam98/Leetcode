#Add "0: 1" in dictionary (base case), for sum == target
#Store prev in HashMap, if remaining (sum-target) in the dictionary, add count by d[sum-target], then add d[sum-target] by 1
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = dict()
        d[0] = 1
        s = 0
        count = 0
        
        for i in range(len(nums)):
            s += nums[i]
            count += d.get(s-k, 0)
            d[s] = d.get(s, 0) + 1
        
        return count

#Slow approach, not accepted(O(n^2))
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(len(nums)):
            s = 0
            for j in range(i, len(nums)):
                s += nums[j]
                if s == k:
                    res += 1
        return res

#Slow approach, not accepted (O(n^3))
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)+1):
                s = 0
                for l in range(i,j):
                    s += nums[l]
                if s == k:
                    count += 1
        
        return count
