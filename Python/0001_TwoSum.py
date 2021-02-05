class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i, e in enumerate(nums):
            if target-e in d:
                return d[target-e], i
            d[e] = i
