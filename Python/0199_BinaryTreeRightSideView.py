# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        res = []
        queue = [root]
        
        while queue:
            temp = []
            for i in range(len(queue)):
                curr = queue.pop(0)
                temp.append(curr.val)
                
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                    
            res.append(temp[-1])
        
        return res
