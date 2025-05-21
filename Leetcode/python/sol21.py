# https://leetcode.com/problems/merge-two-sorted-lists/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        first = list1
        second = list2
        rslt = ListNode(-1)
        dummy = rslt
        while first and second:
            if first.val <= second.val:
                dummy.next = ListNode(first.val)
                dummy = dummy.next
                first = first.next
            else:
                dummy.next = ListNode(second.val)
                dummy = dummy.next
                second = second.next

        if first:
            dummy.next = first
        if second:
            dummy.next = second

        return rslt.next





