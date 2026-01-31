
// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/


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

function lowestCommonAncestor(root: TreeNode | null, p: TreeNode | null, q: TreeNode | null): TreeNode | null {

	let start:TreeNode = root;
    while((p.val < start.val && q.val < start.val) || (p.val > start.val && q.val > start.val)){
        start = p.val < start.val ? start.left : start.right;
    }

    return start;

    // while (!(p.val <= start.val && start.val <= q.val) && !(p.val >= start.val && start.val >= q.val)){
    //     if(p.val > start.val && q.val > start.val){
    //         start = start.right
    //     }else if(p.val < start.val && q.val < start.val){
    //         start = start.left
    //     }
    // }
    // return start;
};