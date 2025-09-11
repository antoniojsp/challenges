
//https://leetcode.com/problems/path-sum/


/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} targetSum
 * @return {boolean}
 */
var hasPathSum = function(root, targetSum) {

   function helper(node, target) {
        if (!node){
            return false;
        }
        if(!node.left && !node.right){
            return target == node.val;
        }
        let new_target = target - node.val
        return (helper(node.left, new_target) || helper(node.right, new_target))
    };

    return helper(root, targetSum);
};