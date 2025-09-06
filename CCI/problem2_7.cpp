

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
    int size(ListNode *node){
        int length = 0;
        while(node){
            length++;
            node = node->next;
        }
        return length;
    }

    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        int len1 = size(headA);
        int len2 = size(headB);

        int gap = abs(len1-len2);

        if (len1 < len2){ // make headA always the longest
            swap(headA, headB);
        }
        ListNode* currA = headA;
        ListNode* currB = headB;

        while(gap>0){
            currA = currA->next;
            gap-=1;
        }

        while (currA && currB){
            if(currA == currB){
                return currA;
            }
            currA = currA->next;
            currB = currB->next;
        }

        return nullptr;
    }
};