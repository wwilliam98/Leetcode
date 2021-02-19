# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        if not root:
            return None
        if not root.left and not root.right:
            if root.val >= limit: #If there is space cap in the limit, return root
                return root
            else: #If there is no space, return None
                return None
        
        root.left = self.sufficientSubset(root.left, limit - root.val)
        root.right = self.sufficientSubset(root.right, limit - root.val)
        if root.left or root.right: 
            return root
