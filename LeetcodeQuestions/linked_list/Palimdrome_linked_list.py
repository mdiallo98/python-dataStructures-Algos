# Given the head of a singly linked list, return true if it is a palindrome.
# Input: head = [1,2,2,1]
# Output: true


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        curr = head

        while curr:
            stack.append(curr.val)
            curr = curr.next

        l, r = 0, len(stack)-1
        while l < r:
            if stack[l] != stack[r]:
                return False
            l += 1
            r -= 1
        return True

    def efficient_Palindrome(self, head):

        fast, slow = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev = None
        curr = slow
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
# The first solution gets it done but it is has a bIG O(n) time complexity and a Space complexity O(n) since we are using extra memory for our Stack and its size may increase as our list Updates.

#  Second method is very efficient its O(n) Time complexity and O(1) constant space due to our use of Pointers
