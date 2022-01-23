#DP
# elements      :   9    5    8    2    -6    4    -3    0    2    -5    15    10    -7    9    -2
# positive_len  :   1    2    3    4     0    1     7    0    1     0     1     2     5    6     5
# negative_len  :   0    0    0    0     5    6     2    0    0     2     3     4     3    4     7
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        dp = [[0]*2 for _ in range(len(nums))]
        if nums[0] > 0:
            dp[0][0] = 1
        elif nums[0] < 0:
            dp[0][1] = 1   
        if len(nums) == 1:
            return dp[0][0]
        
        res = 0
        
        for i in range(1, len(nums)):
            if nums[i] > 0:
                dp[i][0] = dp[i-1][0]+1
                if dp[i-1][1] > 0:
                    dp[i][1] = dp[i-1][1]+1
            
            elif nums[i] < 0:
                if dp[i-1][1] > 0:
                    dp[i][0] = dp[i-1][1]+1
                dp[i][1] = dp[i-1][0]+1
            
            res = max(res, dp[i][0])
        
        return res