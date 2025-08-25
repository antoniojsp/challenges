# https://leetcode.com/problems/merge-in-between-linked-lists/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def find_start_end(self, head:ListNode, a:int, b:int) -> tuple[ListNode, ListNode]:
        '''
        returns pointer thst indicate where to merge list2 into list1
        '''
        start = head
        for _ in range(a-1):
            start = start.next
        end = start
        for _ in range(b - a + 2):
            end = end.next
        return start, end

    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        if not list2:
            return list1
        start, end = self.find_start_end(list1, a, b) # get pointers
        start.next = list2 # merge list2 in the start point in the start pointer
        temp = list2
        while temp.next:
            temp = temp.next
        temp.next = end

        return list1


