# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:
            n = TreeNode(v)
            n.left = root
            return n
        
        self.helper(root, v, d, 1)
        return root
    
    def helper(self, node, v, d, h):
        if node == None:
            return
        
        if h == d - 1:
            newleft = TreeNode(v)
            newright = TreeNode(v)
            prev_left = node.left
            prev_right = node.right
            
            node.left = newleft
            node.right = newright
            node.left.left = prev_left
            node.right.right = prev_right
        
        self.helper(node.left, v, d, h + 1)
        self.helper(node.right, v, d, h + 1)
