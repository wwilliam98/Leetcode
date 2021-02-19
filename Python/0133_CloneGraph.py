"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        self.visited = {}
        return self.helper(node)
        
    def helper(self, n):
        if not n:
            return None
    
        if n in self.visited:
            return self.visited[n]
        
        clone = Node(n.val, [])
        self.visited[n] = clone
        
        for i in n.neighbors:
            clone.neighbors.append(self.helper(i))
        
        return clone
