# https://leetcode.com/problems/linked-list-cycle-ii/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else: # if fast reach None, it means that it can exits normally withou entering to an infinite loop, hence, no cycle
            return None

        slow = head # reset
        while  slow != fast:
            slow = slow.next
            fast = fast.next

        return slow
