# https://leetcode.com/problems/palindrome-linked-list/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        ans = []
        temp = head
        while temp:
            ans.append(temp.val)
            temp = temp.next

        return ans == ans[::-1]




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def print(self, node):
        while node:
            print(node.val)
            node = node.next
        print()

    def reverse(self, node):
        curr = node
        prev = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        if not prev:
            return True
        prev.next = None
        compare = self.reverse(slow)

        while head and compare:
            if head.val != compare.val:
                return False
            head = head.next
            compare = compare.next

        return True




