
//https://leetcode.com/problems/diameter-of-binary-tree/


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

function diameterOfBinaryTree(root: TreeNode | null): number {
    let result = 0;
    const helper = (node:TreeNode | null):number => {
        if(!node){
            return 0;
        }
        let left = helper(node.left);
        let right =  helper(node.right)
        result = Math.max(result, left+right)
        return 1 + Math.max(left, right)
    }

    return result
};