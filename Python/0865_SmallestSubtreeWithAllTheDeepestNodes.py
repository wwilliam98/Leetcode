# Find the deepest nodes using BFS. If there is nothing left in queues, that means all the nodes in current level are the deepest nodes. After we got all the deepest nodes, then we want find the lowest common ancestor (LCA) of all the node using recursion.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        leafs = self.bfs(root)
        return self.LCA(root, leafs)
        
    def bfs(self, node):
        q = [node]
        while q:
            level = []
            for i in range(len(q)):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                level.append(node)
            if not q:
                return level
        
        
    def LCA(self, node, nodes): #nodes going to be list
        if not node:
            return None
        
        if node in nodes:
            return node
        
        left = self.LCA(node.left, nodes)
        right = self.LCA(node.right, nodes)
        
        if left and right:
            return node
        
        else:
            return left or right
