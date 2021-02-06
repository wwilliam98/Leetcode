# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Check after We subtract
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        ret = []
        self.helper(root, targetSum, [], ret)
        return ret
        
    def helper(self, node, target, path, res):
        if not node:
            return
        
        target -= node.val
        path.append(node.val)
        
        if not node.left and not node.right and target == 0:
            res.append(list(path))
            
        self.helper(node.left, target, path, res)
        self.helper(node.right, target, path, res)
        
        path.pop()
#########################################
#Check Before We Subtract
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        ret = []
        self.helper(root, targetSum, [], ret)
        return ret
        
    def helper(self, node, target, path, res):
        if not node:
            return
        
        path.append(node.val)
        
        if not node.left and not node.right and target == node.val:
            res.append(list(path))
            
        self.helper(node.left, target-node.val, path, res)
        self.helper(node.right, target-node.val, path, res)
        
        path.pop()

