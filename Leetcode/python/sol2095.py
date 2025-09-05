#https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/

## Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        slow = head # two pointers, slow and fast. Fast moves 2 times faster than slow, so when fast hit the end, slow is in the middle of the linked list
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        if not prev: # if prev is None, then return None because the list only has one element that needs to be deleted
            return None
        prev.next = prev.next.next # delete middle node
        return head