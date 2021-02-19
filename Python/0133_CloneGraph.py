"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
#DSF (hardcore)
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

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
#BFS
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        
        visited = {}
        q = [node]
        visited[node] = Node(node.val, []) #set map (realnode: clone)
        while q:
            n = q.pop(0)
            
            for neighbor in n.neighbors:
                if neighbor not in visited: #When its not in map, dont put it in the map nor q
                    visited[neighbor] = Node(neighbor.val, [])
                    q.append(neighbor)
                    
                visited[n].neighbors.append(visited[neighbor]) #append cloned neighbor to cloned node neighbor
        
        return visited[node] #Ta-da, just return the node
