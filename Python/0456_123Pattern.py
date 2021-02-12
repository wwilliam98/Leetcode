#Stack, find minimum, store elements from behind, first case: we want to check if nums[i] is greater than min (i < k), then we want to pop the stack if stack[-1] is less than min because we want the number to be greater than min[i] (i < j), if we found something greater than i, return the TRUE
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        
        mini = [-1] * len(nums)
        mini[0] = nums[0]
        stack = []
        for i in range(1, len(nums)):
            mini[i] = min(mini[i-1], nums[i])
            
        for i in range(len(nums)-1, -1, -1):
            if nums[i] <= mini[i]:
                continue
            while stack and stack[-1] <= mini[i]:
                stack.pop()
            if stack and stack[-1] < nums[i]:
                return True
            stack.append(nums[i])
        return False
