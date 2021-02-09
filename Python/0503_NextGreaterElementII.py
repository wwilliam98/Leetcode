class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1] * len(nums)
        stack = []
        
        for i in range(len(nums)-1, -1, -1): #store indexes from largest to smalles to stack
            stack.append(i)
        
        for j in range(len(nums)-1, -1, -1): #we want to check from behind first
            while stack and nums[stack[-1]] <= nums[j]:	#if that number is bigger than the number that comes after that, the rest wont matter for the index before the current index
                stack.pop()
            
            if stack: #if we found a number that is bigger, we want to set that number to the result
                res[j] = nums[stack[-1]]
            
            stack.append(j) #dont forget to append the largest number index to the stack
        
        return res


#Brute force, most circular array can be solved by adding the 2x the array
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        temp = nums + nums[:len(nums)-1]
        
        res = []
        for i in range(len(nums)):
            for j in range(i+1, len(temp)):
                if nums[i] < temp[j]:
                    res.append(temp[j])
                    break
            else:
                res.append(-1)
        return res
