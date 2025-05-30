
// https://leetcode.com/problems/linked-list-cycle/description/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {

        ListNode* curr = head;
        set<ListNode*> seen;
        while(curr){
            if (seen.count(curr) > 0){
                return true;
            }
            seen.insert(curr);
            curr = curr->next;
        }

        return false;
    }
};