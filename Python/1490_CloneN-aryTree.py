"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        #basecase
        if not root:
            return None
        
        #map (node, clone)
        d = collections.defaultdict(list)
        
        #set q, and map for first root
        q = [root]
        d[root] = Node(root.val, [])
        
        #loop
        while q:
            n = q.pop(0)
            #look through each child
            for child in n.children:
                d[child] = Node(child.val, []) #Clone the child first before putting as children for the node
                q.append(child)
                d[n].children.append(d[child])
        
        return d[root]
