# https://leetcode.com/problems/merge-nodes-in-between-zeros/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return head

        curr_sum = 0
        start = head
        curr_node = head.next # starts from the next value from the start

        while curr_node:
            if curr_node.val != 0: # if val is non zero, accumulate the values so far
                curr_sum += curr_node.val
            else: # if zero, modify the zero node with the sum so far, reset the accumulator and link the curr_node with the start
                curr_node.val = curr_sum
                curr_sum = 0
                start.next = curr_node
                start = curr_node
            curr_node = curr_node.next

        return head.next # the first element of the original linkedlist is use as dummy, the result is linked after it

