# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        self.binary = []
        self.helper(root, 0)
        s = 0
        for n in self.binary:
            s += int(str(n), 2)
        return s
        
    def helper(self, node, temp):
        temp = temp * 10 + node.val
        if not node.left and not node.right:
            self.binary.append(temp)
            return
        
        if node.left:
            self.helper(node.left, temp)
        if node.right:
            self.helper(node.right, temp)
