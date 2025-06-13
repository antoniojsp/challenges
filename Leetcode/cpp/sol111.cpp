

// https://leetcode.com/problems/minimum-depth-of-binary-tree/

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
    int minDepth(TreeNode* root) {

        if(!root){
            return 0;
        }
        deque<pair<TreeNode*, int>> Q;
        Q.push_back({root, 1});

        while(!Q.empty()){
            auto [current, level] = Q.front();
            Q.pop_front();
            if (!current->left && !current->right){
                return level;
            }
            if(current && current->left){
                Q.push_back({current->left, level+1});
            }
            if(current && current->right){
                Q.push_back({current->right, level+1});
            }
        }

        return -1;
    }
};