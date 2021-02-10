# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.inorder = []
        self.index = -1
        self.recur(root)
    
    def recur(self, node):
        if not node:
            return
        
        self.recur(node.left)
        self.inorder.append(node.val)
        self.recur(node.right)

    def next(self) -> int:
        self.index += 1
        return self.inorder[self.index]

    def hasNext(self) -> bool:
        return self.index + 1 < len(self.inorder)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
