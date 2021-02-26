# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ret = None
        self.dfs(root, p ,q)
        return self.ret
        
    def dfs(self, node, p ,q):
        if not node:
            return False
        
        left = self.dfs(node.left, p, q)
        right = self.dfs(node.right, p, q)
        
        flag = node == p or node == q
        
        if left + right + flag >= 2:
            self.ret = node
        
        return flag or left or right
