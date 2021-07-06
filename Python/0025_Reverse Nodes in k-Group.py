class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        counter = 0
        curr = head

        while counter < k and curr:
            curr = curr.next
            counter += 1

        if counter == k:
            #reverse from the head until k
            reversedHead = self.reverseList(head, k)

            #after reverse, head becomes the tail and tail goes to the next
            head.next = self.reverseKGroup(curr, k)
            return reversedHead
        return head


    def reverseList(self, head, k):
        prev, curr = None, head
        while k:
            #swap
            curr.next, prev, curr = prev, curr, curr.next

            k-= 1
        return prev
