# https://leetcode.com/problems/add-two-numbers/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # for testing
    # def print(self, node):
    #     while node:
    #         print(node.val, end = " ")
    #         node = node.next
    #     print()

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        remainder = 0
        rslt = ListNode(-1)
        dummy = rslt
        while l1 or l2 or remainder: # keep adding till there are no
            curr_suma = remainder # add remainder if any
            if l1:
                curr_suma+=l1.val
                l1 = l1.next
            if l2:
                curr_suma+=l2.val
                l2 = l2.next

            digit, remainder = curr_suma%10, curr_suma//10

            dummy.next = ListNode(digit)
            dummy = dummy.next

        return rslt.next

