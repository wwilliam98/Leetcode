# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        greater_curr = greater_head = ListNode(0)
        smaller_curr = smaller_head = ListNode(0)
        
        while head:
            if head.val >= x:
                greater_curr.next = head
                greater_curr = greater_curr.next
                
            else:
                smaller_curr.next = head
                smaller_curr = smaller_curr.next
            
            head = head.next
            
        greater_curr.next = None
        smaller_curr.next = greater_head.next
        
        return smaller_head.next
