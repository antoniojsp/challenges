
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



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        result = self.head.val

        curr = self.head
        i = 1
        while curr:
            if random.randint(1, i) == 1:
                result = curr.val
            curr = curr.next
            i+=1

        return result

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        result = self.head.val
        curr = self.head
        i = 1
        while curr:
            if random.randint(1, i) == 1:
                result = curr.val
            curr = curr.next
            i+=1

        return result

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()


