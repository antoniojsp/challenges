

https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

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
// if even left to right
// if odd right to left
    void helper(TreeNode* node, int level, vector<deque<int>>& res){
        if(!node){
            return;
        }
        if(level == res.size()){
            res.push_back({});
        }

        if (level%2 == 0){
            res[level].push_back(node->val);
        }else{
            res[level].push_front(node->val);
        }

        helper(node->left, level+1, res);
        helper(node->right, level+1, res);
    }

    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        if (!root){
            return {};
        }
        vector<deque<int>> res;
        helper(root, 0, res);
        vector<vector<int>> result(res.size());
        for (int i = 0; i<res.size(); i++){
            for(auto val:res[i]){
                result[i].push_back(val);
            }
        }

        return result;
    }
};