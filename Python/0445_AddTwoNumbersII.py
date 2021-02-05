# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head1 = self.ReverseList(l1)
        head2 = self.ReverseList(l2)
        
        prev = None
        carry = 0
        while head1 or head2:
            if head1:
                num1 = head1.val
            if not head1:
                num1 = 0
            if head2:
                num2 = head2.val
            if not head2:
                num2 = 0
        
            s = (carry + num1 + num2) % 10
            carry = (carry + num1 + num2) // 10
            
            print(s, carry)
            node = ListNode(s)
            node.next = prev
            prev = node
            
            if head1:
                head1 = head1.next
            if head2:
                head2 = head2.next
        
        if carry:
            curr = ListNode(carry)
            curr.next = prev
            prev = curr
        
        return prev
    
    
    def ReverseList(self, head):
        dummy = None
        prev, curr = dummy, head
        
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        
        return prev
