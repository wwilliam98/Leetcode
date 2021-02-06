# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.helper(root)
        
    def helper(self, node):
        #base case, if its not a node just return None
        if not node:
            return None
        
        #if its leaf, return the node
        if not node.left and not node.right:
            return node
        
        #recurse left and right
        leftnode = self.helper(node.left)
        rightnode = self.helper(node.right)
        
        #if there is leftTail, we want to manipulate the node
        #most left connect to right, then set node.right become node.left
        if leftnode:
            leftnode.right = node.right
            node.right = node.left
            node.left = None
            
        #return the right most node
        if rightnode:
            return rightnode
        else:
            return leftnode
