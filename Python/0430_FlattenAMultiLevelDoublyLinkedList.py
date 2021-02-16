"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return None
        
        dummy = Node(0, None, head, None)
        stack = [head]
        pre = dummy
        
        while stack:
            curr = stack.pop()
            curr.prev = pre
            pre.next = curr
            
            if curr.next:
                stack.append(curr.next)
                curr.next = None
            
            if curr.child:
                stack.append(curr.child)
                curr.child = None
            
            pre = curr
        dummy.next.prev = None #We dont want to connect anything to the dummy
        return dummy.next
