# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if not head:
            return None
        length = 0
        current = head
        while  current:
            length +=1
            current = current.next

        if n == length: # if there is one element, and n = 1
            return head.next

        count = 0
        current = head
        while count < length - n - 1:
            current = current.next
            count+=1
        current.next = current.next.next

        return head