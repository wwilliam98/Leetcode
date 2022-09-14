# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        counter = [0] * 9
        return self.helper(root, counter)
        
    def helper(self, root, counter):
        if not root:
            return 0
        
        arr = [0] * 9
        arr[root.val-1] += 1
        
        if not root.left and not root.right:
            return int(self.pseudopalindromic([x + y for (x, y) in zip(counter, arr)]))
        
        left = self.helper(root.left, [x + y for (x, y) in zip(counter, arr)])
        right = self.helper(root.right, [x + y for (x, y) in zip(counter, arr)])
        return left + right
    
    # if there is more than 1 odd, then it cannot be a palindrome
    def pseudopalindromic(self, nums):
        odd = 0
        for i in range(9):
            if nums[i] % 2 == 1:
                odd += 1
                
                if odd > 1:
                    return False
        return True

# Solution 2
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def traverse(node, pairs):
            if not node:
                return 0
            
            # If there is a pair in the set, then just remove them because 2 occurance will be a palindrome
            if node.val in pairs:
                pairs.remove(node.val)
            else:
                pairs.add(node.val)
            
            if not node.left and not node.right:
                return 1 if len(pairs) <= 1 else 0
            
            # correct!!
            left = traverse(node.left, set(pairs))
            right = traverse(node.right, set(pairs))
            
            # wrong, becasue pairs will change after we traversed node.left or node.right!
            # left = traverse(node.left, pairs)
            # right = traverse(node.right, pairs)
            
            return left + right
        
        return traverse(root, set())