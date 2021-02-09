# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        res = []
        stack = []
        
        while head:
            while stack and stack[-1][1] < head.val: #if there is stack and the top value is less then the current val, res with index stack = val
                res[stack.pop()[0]] = head.val
                
            stack.append([len(res), head.val])  #store the index and value
            res.append(0)
            head = head.next
        
        return res
