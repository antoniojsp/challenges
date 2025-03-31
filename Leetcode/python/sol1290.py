#  https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        binary = []
        while head:
            binary = [head.val] + binary
            head = head.next
        result = [binary[i ] *( 2* *i) for i in range(len(binary))]
        return sum(result)


