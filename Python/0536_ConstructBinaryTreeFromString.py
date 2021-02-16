# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> TreeNode:
        firstIdx = s.find("(")
        if firstIdx < 0:
            if s:
                return TreeNode(int(s))
            else:
                return None
        
        flag = 0
        for lastIdx, e in enumerate(s):
            if e == "(":
                flag += 1
            if e == ")":
                flag -= 1
            if lastIdx > firstIdx and flag == 0:
                break
                
        root = TreeNode(int(s[:firstIdx]))
        root.left = self.str2tree(s[firstIdx+1:lastIdx])
        root.right = self.str2tree(s[lastIdx+2:-1])
        
        return root
