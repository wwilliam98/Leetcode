## DFS, mark a flag if its, p or q. If True is more than 2, set the answer.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ret = None
        self.dfs(root, p ,q)
        return self.ret
        
    def dfs(self, node, p ,q):
        if not node:
            return False
        
        flag = node == p or node == q
        left = self.dfs(node.left, p, q)
        right = self.dfs(node.right, p, q)
        
        if left + right + flag >= 2:
            self.ret = node
        
        return flag or left or right

## Queue, put the parents in dictionary, put all ancestors of p in set, find q that is in the ancestors
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        queue = [root]
        parents = {root: None}
        
        while p not in parents or q not in parents:
            node = queue.pop(0)
            if node.left:
                parents[node.left] = node
                queue.append(node.left)
                
            if node.right:
                parents[node.right] = node
                queue.append(node.right)
                
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parents[p]
        
        while q not in ancestors:
            q = parents[q]
        
        return q
