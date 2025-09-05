
//https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        length = 0
        current = head
        while  current:
            length +=1
            current = current.next

        if n == length: # if there is one element, and n = 1
            return head.next

        count = 0
        current = head
        while count < length - n - 1:
            current = current.next
            count+=1
        current.next = current.next.next

        return head


/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* dummy = new ListNode(-1, head); // adding dummy node at the beginning
        ListNode* first = dummy; //first node move n times forward
        ListNode* second = dummy;  // once first position is found, second starts moving forward too.
        for(int i = 0; i < n; i++){
            first = first->next;
        }
        while(first->next){ // when first hit the of the list, second stop, delivering the node previous to the result
            second = second->next;
            first = first->next;
        }
        second->next = second->next->next; // node removed
        ListNode* result = dummy->next;
        delete dummy;
        return result;
    }
};