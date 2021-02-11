"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        self.visited = {}
        return self.helper(head)
        
    def helper(self, oldhead):
        if not oldhead:
            return None
        
        if oldhead in self.visited: #if the random pointer, pointing to the previous node, return new node
            return self.visited[oldhead]
        
        newHead = Node(oldhead.val, None, None)
        self.visited[oldhead] = newHead
    
        newHead.next = self.helper(oldhead.next)
        newHead.random = self.helper(oldhead.random)
        
        return newHead
