# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: TreeNode, p: int, q: int) -> int:
        lca = self.LCA(root, p, q)
        return self.dist(lca, p) + self.dist(lca, q)
        
    def LCA(self, node, p, q):
        if not node or node.val == p or node.val == q:
            return node
        
        left = self.LCA(node.left, p, q)
        right = self.LCA(node.right, p, q)
        
        if left and right:
            return node
        else:
            return left or right
    
    def dist(self, node, dest):
        if not node:
            return float('inf')
        
        if node.val == dest:
            return 0
        
        return 1 + min(self.dist(node.left, dest), self.dist(node.right, dest))
