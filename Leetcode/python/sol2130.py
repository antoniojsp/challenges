
# https://leetcode.com/problems/rings-and-rods/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # size of linked list
        temp = head
        size = 0
        while temp:
            size += 1
            temp = temp.next
        # move pointer
        middle = head
        i = 0
        while i < size // 2:
            i += 1
            middle = middle.next

        # reverse second half
        reverse = middle
        prev = None
        while reverse:
            next_elem = reverse.next
            reverse.next = prev
            prev = reverse
            reverse = next_elem

        # compare
        max_sum = 0
        while prev:
            max_sum = max(max_sum, prev.val + head.val)
            head = head.next
            prev = prev.next

        return max_sum


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # size of linked list
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # # reverse second half
        reverse = slow
        prev = None
        while reverse:
            next_elem = reverse.next
            reverse.next = prev
            prev = reverse
            reverse = next_elem

        max_sum = 0
        first, second = head, prev
        while second:
            max_sum = max(max_sum, first.val + second.val)
            first = first.next
            second = second.next

        return max_sum




