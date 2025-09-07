# https://leetcode.com/problems/add-two-numbers-ii/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, node):
        curr = node
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = self.reverse(l1) # reverse number since least significant digit is at the end
        l2 = self.reverse(l2)
        remainder = 0 # keep tracks if the sum of two digits is greater than 9 (i.e 15 carry 1)
        dummy = ListNode(-1)
        rslt = dummy
        while l1 or l2 or remainder:
            temp = remainder
            if l1:
                temp+=l1.val
                l1 = l1.next
            if l2:
                temp+=l2.val
                l2 = l2.next
            rslt.next = ListNode(temp%10)
            rslt = rslt.next
            remainder = temp//10

        return self.reverse(dummy.next)