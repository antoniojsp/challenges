# https://leetcode.com/problems/remove-nodes-from-linked-list/solutions/7129270/double-memory-version-by-antoniojsp-gjdb/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def print(self, node):
        while node:
            print(node.val, end=" ")
            node = node.next
        print()

    def reverse(self, head):
        current = head
        prev = None
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev


    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = self.reverse(head) # reverse the list, and then explore from right to left, keeping the max value so far

        dummy = ListNode(-1) # by constraint, all numbers are
        max_val = -1
        tail = dummy

        current = head
        while current:
            if current.val >= max_val:
                max_val = current.val
                tail.next = ListNode(current.val)
                tail = tail.next
            current = current.next

        return self.reverse(dummy.next)





