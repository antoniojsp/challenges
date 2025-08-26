# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        result:int = 0
        while head:
            result = result * 2 + head.val
            head = head.next

        return result


        # binary = []
        # while head:
        #     binary = [head.val] + binary
        #     head = head.next
        # result = [binary[i]*(2**i) for i in range(len(binary))]
        # return sum(result)


