# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#Check if its mirrored
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.helper(root, root)
        
    def helper(self, left, right): #Check if its mirror, left == right, right == left
        if not left and not right:
            return True
        if not left or not right:
            return False
        
        return (left.val == right.val) and self.helper(left.left, right.right) and self.helper(right.left, left.right)

####################################
#Check left, and right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        return self.helper(root.left, root.right)
        
    def helper(self, left, right):
        if left and right:
            return left.val == right.val and self.helper(left.left, right.right) and self.helper(left.right, right.left)
        
        else:
            return left == right
