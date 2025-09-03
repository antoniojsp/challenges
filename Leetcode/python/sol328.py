# https://leetcode.com/problems/odd-even-linked-list/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        i = 1
        odd = []
        even = []
        while current:
            if i% 2 == 0:
                even.append(current.val)
            else:
                odd.append(current.val)
            i += 1
            current = current.next

        dummy = ListNode(-1)
        rslt = dummy
        for i in odd + even:
            dummy.next = ListNode(i)
            dummy = dummy.next

        return rslt.next



