"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        self.first, self.last = None, None
        if not root:
            return root
        
        self.helper(root)
        self.first.left = self.last
        self.last.right = self.first
        return self.first
        
        
    def helper(self, node):
        if node:
            self.helper(node.left)
            
            if self.last:
                self.last.right = node
                node.left = self.last
                
            else:
                self.first = node
            self.last = node
            
            self.helper(node.right)
