class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = prev = ListNode(-1)
        dummy.next = head
        prev, curr = dummy, head

        while curr:
            #Remove duplicate
            if curr.next and curr.val == curr.next.val:
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                curr = curr.next #Remove the last duplicate
                prev.next = curr

            else:
                prev = prev.next
                curr = curr.next
        return dummy.next
