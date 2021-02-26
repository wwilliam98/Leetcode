# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Node') -> 'NodeCopy':
        self.d = {}
        return self.dfs(root)
        
    def dfs(self, node):
        if not node:
            return None
        
        if node in self.d:
            return self.d[node]
        
        newNode = NodeCopy(node.val)
        
        self.d[node] = newNode
        
        newNode.left = self.dfs(node.left)
        newNode.right = self.dfs(node.right)
        newNode.random = self.dfs(node.random)
        
        return newNode
