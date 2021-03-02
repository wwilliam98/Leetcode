# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        leaves = self.bfs(root)
        return self.LCA(root, leaves)
        
    def bfs(self, node):
        q = [node]
        while q:
            level = []
            for i in range(len(q)):
                n = q.pop(0)
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
                level.append(n)
            
            if not q:
                return level
        
        
    def LCA(self, node, leaves):
        if not node:
            return None
        
        if node in leaves:
            return node
        
        left = self.LCA(node.left, leaves)
        right = self.LCA(node.right, leaves)
        
        if left and right:
            return node
        
        else:
            return left or right
