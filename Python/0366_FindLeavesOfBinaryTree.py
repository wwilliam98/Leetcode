# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        self.res = []
        self.leaf = []
        while root:
            root = self.dfs(root)
            self.res.append(self.leaf)
            self.leaf = []
        return self.res
        
    def dfs(self, node):
        if not node:
            return None
        if not node.left and not node.right:
            self.leaf.append(node.val)
            return None
        else:
            node.left = self.dfs(node.left)
            node.right = self.dfs(node.right)
            return node
