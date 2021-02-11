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
        self.hash = {}
        return self.helper(head)
        
    def helper(self, oldhead):
        if not oldhead:
            return None
        
        if oldhead in self.hash:
            return self.hash[oldhead]
        
        newHead = Node(oldhead.val, None, None)
        self.hash[oldhead] = newHead
        
        newHead.next = self.helper(oldhead.next)
        newHead.random = self.helper(oldhead.random)
        
        return newHead
