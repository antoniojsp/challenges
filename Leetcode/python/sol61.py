# https://leetcode.com/problems/rotate-list/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def length(self, temp) -> int:
        length = 0
        while temp:
            length+=1
            temp=temp.next
        return length

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        size = self.length(head)

        if size <= 1 or k == 0:
            return head

        pos = size - (k % size ) -1

        cut = head
        for _ in range(pos):
            cut = cut.next

        temp = head
        while temp.next:
            temp = temp.next
        temp.next = head
        head = cut.next
        cut.next = None
        return head

