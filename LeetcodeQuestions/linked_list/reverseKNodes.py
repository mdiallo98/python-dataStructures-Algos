class Solution:
    def reverseKGroup(self, head, k):
        # since this will be a recursive function we need to make sure the context is restate for each recursive call
        curr = head
        count = 0

        while curr and count != k:
            curr = curr.next
            count += 1
        #  if we have enough values to do the reversing then we can go ahead and do it

        if count == 1:

            reversedHead = self.reverseList(head, k)
            head.next = self.reverseKGroup(curr, k)
            return reversedHead
        return head

    def reverseList(head, k):
        prev, curr = None, head
        while k:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            k -= 1
        return prev
