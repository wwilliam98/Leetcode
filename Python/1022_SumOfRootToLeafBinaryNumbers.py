# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        self.s = 0
        self.helper(root, 0)
        return self.s
        
    def helper(self, node, temp):
        temp = temp * 10 + node.val
        if not node.left and not node.right:
            self.s += int(str(temp), 2)
            return
        
        if node.left:
            self.helper(node.left, temp)
        if node.right:
            self.helper(node.right, temp)
