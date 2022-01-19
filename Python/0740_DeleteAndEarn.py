#Memoization
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        freq = [0] * (max(nums)+1)
        for n in nums:
            freq[n] += n
            
        memo = {}
        memo[0] = 0
        memo[1] = freq[1]
        
        for i in range(2, len(freq)):
            memo[i] = max(memo[i-1], memo[i-2] + freq[i])
        return memo[len(freq)-1]