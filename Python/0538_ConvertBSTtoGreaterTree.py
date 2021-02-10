def convertBST(self, root: TreeNode) -> TreeNode:
        self.cur = 0
        return self.dfs(root)
    
    def dfs(self, node):
        if not node:
            return
        
        self.dfs(node.right)
        self.cur += node.val
        node.val = self.cur
        self.dfs(node.left)
        
        return node
