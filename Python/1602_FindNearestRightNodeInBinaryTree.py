# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> TreeNode:
        if not root:
            return None
        
        q = [root]
        while q:
            flag = False
            level = []
            for i in range(len(q)):
                node = q.pop(0)
                level.append(node)
                if node == u:
                    flag = True
                    index = i
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if flag == True:
                if index == len(level)-1:
                    return None
                else:
                    return level[index+1]
