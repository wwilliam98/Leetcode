#Iteratively
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        prev_tail, curr = None, head
        ret = None

        while curr:
            counter = 0
            head = curr

            while counter < k and curr:
                curr = curr.next
                counter += 1

            if counter == k:
                reversedHead = self.reverseList(head, k)

                if not ret:
                    ret = reversedHead

                if prev_tail:
                    prev_tail.next = reversedHead

                prev_tail = head
                head = curr

        if prev_tail:
            prev_tail.next = head

        return ret if ret else head

    def reverseList(self, head, k):
        prev, curr = None, head

        while k:
            curr.next, prev, curr = prev, curr, curr.next
            k-=1

        return prev

#Recursion time = O(n), space = O(n)
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
