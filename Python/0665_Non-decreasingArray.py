class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        #Switch the first occurance to the greater one or switch the greater one to the smaller one
        #if either one is sorted then its Possible
        one, two = nums[:], nums[:]
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                one[i] = nums[i + 1]
                two[i + 1] = nums[i]
                break
        return one == sorted(one) or two == sorted(two)