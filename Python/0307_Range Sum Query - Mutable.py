class Node():
    def __init__(self, start, end): #start, end is like the value/identifier
        self.left = None
        self.right = None
        self.start = start
        self.end = end
        self.total = 0

class NumArray:

    def __init__(self, nums: List[int]):
        def create_tree(nums, l, r):
            if l > r:
                return None
            
            if l == r:
                node = Node(l, r)
                node.total = nums[l]
                return node
            
            mid = (l+r) // 2
            
            root = Node(l, r)
            root.left = create_tree(nums, l, mid)
            root.right = create_tree(nums, mid+1, r)
            
            root.total = root.left.total + root.right.total
            return root
        self.root = create_tree(nums, 0, len(nums)-1)

    def update(self, index: int, val: int) -> None:
        def updateval(root, i, val):
            if root.start == root.end:
                root.total = val
                return root.total
            
            mid = (root.start + root.end) // 2
            if i <= mid:
                updateval(root.left, i, val)
            else:
                updateval(root.right, i, val)
            
            root.total = root.left.total + root.right.total
            return root.total
        
        updateval(self.root, index, val)

    def sumRange(self, left: int, right: int) -> int:
        def node_sum(root, l, r):
            if root.start == l and root.end == r:
                return root.total
            
            mid = (root.start + root.end) // 2
            
            if r <= mid:
                return node_sum(root.left, l, r)
            
            elif l >= mid + 1:
                return node_sum(root.right,l, r)
            
            else:
                return node_sum(root.left, l, mid) + node_sum(root.right,mid+1 ,r)
            
        return node_sum(self.root, left, right)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)