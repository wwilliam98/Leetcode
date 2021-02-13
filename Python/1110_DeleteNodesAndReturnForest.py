# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        self.res = []
        self.dfs(root, to_delete)
        
        if root.val not in to_delete:
            self.res.append(root)
        
        return self.res
        
        
    def dfs(self, node, dVal):
        if not node:
            return None
        
        node.left = self.dfs(node.left, dVal)
        node.right = self.dfs(node.right, dVal)
        
        if node.val in dVal:
            if node.left:
                self.res.append(node.left)
            if node.right:
                self.res.append(node.right)
            return None
        
        return node
