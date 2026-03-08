
//https://leetcode.com/problems/increasing-order-search-tree/description/

/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function increasingBST(root: TreeNode | null): TreeNode | null {
    let dummy = new TreeNode(-1);
    let temp = dummy
    const helper = (node) => {
        if(!node){
            return;
        }
        helper(node.left)
        temp.right = new TreeNode(node.val)
        temp = temp.right
        helper(node.right)
    }
    helper(root)
    return dummy.right;
};