class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        
        i1, i2 = 0, len(nums)-1
        while i1 < len(nums)-1 and nums[i1] <= nums[i1+1]:
            i1 += 1
        
        while i2 > 0 and nums[i2] >= nums[i2-1]:
            i2 -= 1
        
        if i1 > i2:
            return 0
        
        minVal = min(nums[i1:i2+1])
        maxVal = max(nums[i1:i2+1])
        
        while i1 > 0 and minVal < nums[i1-1]:
            i1 -= 1
        
        while i2 < len(nums)-1 and nums[i2+1] < maxVal:
            i2 += 1
        
        return i2-i1+1
