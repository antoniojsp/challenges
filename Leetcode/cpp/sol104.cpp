//https://leetcode.com/problems/maximum-depth-of-binary-tree/description//

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
    int maxDepth(TreeNode* root) {
        if(root == nullptr){
            return 0;
        }
        queue <pair<TreeNode*, int>> Q;
        int max_depth = 0;
        Q.push({root, 1});
        while(!Q.empty()){
            pair<TreeNode*, int> temp = Q.front();
            Q.pop();
            max_depth = max(max_depth, temp.second);
            if(temp.first->left != nullptr){
                Q.push({temp.first->left, temp.second+1});
            }
            if(temp.first->right != nullptr){
                Q.push({temp.first->right, temp.second+1});
            }
        }

        return max_depth;
    }
};

class Solution {
public:
    int maxDepth(TreeNode* root) {

        if (root == nullptr){
            return 0;
        }
        return 1 + max(maxDepth(root->left), maxDepth(root->right));
    }
};