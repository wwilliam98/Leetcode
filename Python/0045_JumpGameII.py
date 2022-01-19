class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        furthest = 0
        marker = 0
        for i in range(len(nums)-1):
            furthest = max(furthest, i + nums[i])
            if i == marker:
                jumps += 1
                marker = furthest
            print(marker)
        return jumps