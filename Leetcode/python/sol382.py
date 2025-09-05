
# https://leetcode.com/problems/linked-list-random-node/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.length = 0
        temp = head
        while temp:
            self.length+=1
            temp = temp.next

    def getRandom(self) -> int:
        rand = random.randint(0, self.length -1)
        result = 0
        curr = self.head
        for i in range(rand):
            curr = curr.next

        return curr.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()