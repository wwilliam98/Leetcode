#sort and find sum less than K, O(n log n)
class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return -1
        
        nums.sort()
        p1, p2 = 0, len(nums)-1
        res = -1
        while p1 < p2:
            s = nums[p1] + nums[p2]
            if s < k:
                res = max(res, s)
                p1 += 1
            else:
                p2 -= 1
        return res

#Slow Solution O(n^2)
class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return -1
        
        mx = -1
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                s = nums[i] + nums[j]
                if s > mx and s < k:
                    mx = s
        return mx
