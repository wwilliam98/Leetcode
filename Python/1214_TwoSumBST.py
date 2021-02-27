# O(m+n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        self.s = set()
        self.storeSet(root1, target)
        print(self.s)
        return self.check(root2)
        
    def storeSet(self, root, target):
        if not root:
            return
        self.storeSet(root.left, target)
        self.s.add(target-root.val)
        
        if root.right:
            self.storeSet(root.right, target)
    
    def check(self, root):
        if not root:
            return
        if root.val in self.s:
            return True
        left = self.check(root.left)
        right = self.check(root.right)
        return left or right
