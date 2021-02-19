# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return None
        
        d = collections.defaultdict(list)
        q = [(root, 0)]
        res = []
        while q:
            node, col = q.pop(0)
            d[col].append(node.val)
            if node.left:
                q.append((node.left, col-1))
            if node.right:
                q.append((node.right, col+1))
                
        for k in sorted(d):
            res.append(d[k])
        return res
