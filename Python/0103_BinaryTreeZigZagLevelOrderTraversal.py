# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        h = 0
        queue = [root]
        
        while queue:
            level = []
            for i in range(len(queue)):
                temp = queue.pop(0)
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
                level.append(temp.val)
            if h % 2 == 1:
                res.append(level[::-1])
            else:
                res.append(level)
            h += 1
        return res
