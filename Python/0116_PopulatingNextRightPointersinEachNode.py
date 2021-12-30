#BFS
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        queue = [root]
        
        while queue:
            number_of_nodes = len(queue)
            for i in range(number_of_nodes):
                node = queue.pop(0)
                if i == (number_of_nodes-1):
                    node.next = None
                else:
                    node.next = queue[0]
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return root

#Iteratively
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        cur  = root
        nx = root.left

        while cur.left :
            cur.left.next = cur.right
            if cur.next:
                cur.right.next = cur.next.left
                cur = cur.next
            else:
                cur = nx
                nx = cur.left
            
        return root