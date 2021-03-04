# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        res = None
        stack1 = []
        stack2 = []
        while headA:
            stack1.append(headA)
            headA = headA.next
        
        while headB:
            stack2.append(headB)
            headB = headB.next
            
        while (stack1 and stack2 and stack1[-1] == stack2[-1]):
            res = stack1.pop()
            stack2.pop()
        
        return res
