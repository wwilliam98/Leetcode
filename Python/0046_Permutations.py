class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        tmp = []
        self.helper(res, tmp, nums)
        return res
        
    def helper(self, res, tmp, nums):
        if len(tmp) == len(nums):
            print (tmp)
            res.append(tmp.copy())
            return
        
        for num in nums:
            if num not in tmp:
                tmp.append(num)
                self.helper(res, tmp, nums)
                tmp.pop()
