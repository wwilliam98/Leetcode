# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        print(inorder, postorder)
        if not inorder or not postorder: #if we keep going right, they left will be gone
            return None
            
        idx = inorder.index(postorder.pop())
        root = TreeNode(inorder[idx])
        root.right = self.buildTree(inorder[idx+1:], postorder) #keep going right because if we go left, it wont match with the postorder pattern
        root.left = self.buildTree(inorder[:idx], postorder)
        
        return root
