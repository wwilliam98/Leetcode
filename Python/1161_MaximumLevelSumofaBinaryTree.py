# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        queue = [root]
        mxLevel, currLevel = 0, 0
        mxSum = float("-inf")
        while queue:
            currLevel += 1
            s = 0
            for i in range(len(queue)):
                curr = queue.pop(0)
                s += curr.val
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            if s > mxSum:
                mxSum = s
                mxLevel = currLevel
        return mxLevel
