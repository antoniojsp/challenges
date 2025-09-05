# https://leetcode.com/problems/intersection-of-two-linked-lists/description/?utm_source=chatgpt.com
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        seen = set()
        currA = headA
        while currA:
            seen.add(currA)
            currA = currA.next

        currB = headB
        while currB: # if node seen in currB presented in seen set, then it means there is a intersection
            if currB in seen:
                return currB
            currB = currB.next

        return None # no intersection found



