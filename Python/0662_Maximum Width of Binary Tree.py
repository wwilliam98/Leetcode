class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0

        max_width = 0
        queue = [(root, 0)] #root, level_node_index

        while queue:
            _, level_node_index = queue[0]

            for i in range(len(queue)):
                node, curr_index = queue.pop(0)

                if node.left:
                    queue.append([node.left, 2 * curr_index])
                if node.right:
                    queue.append([node.right, 2 * curr_index + 1])
                    
            #most right index - most left inded + 1 will be the width of the level
            max_width = max(max_width, curr_index - level_node_index + 1)

        return max_width
