# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        def left(node):
            if not node or not node.left and not node.right: #Return when its a child
                return
            res.append(node.val)
            if node.left:
                left(node.left)
            else: #Only Goes to the Right when there is no left
                left(node.right)
        
        def right(node):
            if not node or not node.left and not node.right: #Return when its a child
                return
            if node.right:
                right(node.right)
            else: #Go left when there is no right
                right(node.left)
            res.append(node.val)
        
        def leaf(node):
            if not node:
                return
                
            if node != root and not node.left and not node.right:
                res.append(node.val)
                
            if node.left:
                leaf(node.left)
                
            if node.right:
                leaf(node.right)
            
        res = [root.val]
        left(root.left)
        leaf(root)
        right(root.right)
        return res
