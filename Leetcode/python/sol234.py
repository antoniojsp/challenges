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
