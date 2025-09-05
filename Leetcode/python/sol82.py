# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # def print(self, node) -> None:
    #     '''
    #     Helper function for testing
    #     '''
    #     while node:
    #         print(node.val, end=" ")
    #         node = node.next
    #     print()

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        dummy = ListNode(-1, head) # create dummy node and use it as a head
        curr = head # current node being visited
        prev = dummy # previous node

        while curr and curr.next:
            next_node = curr.next # save the next node
            if curr.val == curr.next.val: # if current and next node have same value, search next diff value
                dup_val = curr.val
                while curr and curr.val == dup_val :
                    curr = curr.next
                prev.next = curr
            else:
                prev = curr # current node become previous for next loop
                curr = next_node # move forward

        return dummy.next # cut dummy node (ListNode(-1))

