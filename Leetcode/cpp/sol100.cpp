
// https://leetcode.com/problems/same-tree/description/

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {

        if(!p && !q){ // if both end up to nullptr, return true
            return true;
        }
        if(!(p && q)){ // if p is null and q not, or viceverse, then trees have not similar shape, hence, the tree is not equal
            return false;
        }

        if(p->val != q->val){ // check that the values are the same, if it fails, return false
            return false;
        }

        return isSameTree(p->left, q->left) && isSameTree(p->right, q->right); // we use && since any of the base cases returns false, then all is false.

    }
};