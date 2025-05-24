
//https://leetcode.com/problems/remove-linked-list-elements/description/
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
    ListNode* removeElements(ListNode* head, int val) {

        ListNode dummy(-1, head);
        ListNode* prev = &dummy;
        ListNode* current = head;

        while(current){
            if(current->val == val){
                prev->next = current->next;
            }else{
                prev = prev->next;
            }
            current = current->next;
        }

        return dummy.next;
    }
};