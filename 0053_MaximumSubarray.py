class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #DP, Kadane's Algorithm (figure out when a part of the array is worth keeping)
        curr_sub = 0
        mx = float("-inf")
        for n in nums:
            curr_sub += n
            mx = max(mx, curr_sub)
            if curr_sub < 0:
                curr_sub = 0
        
        return mx