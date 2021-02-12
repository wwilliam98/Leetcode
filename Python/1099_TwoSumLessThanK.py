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
