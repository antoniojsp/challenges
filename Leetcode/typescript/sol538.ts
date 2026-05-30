
//https://leetcode.com/problems/convert-bst-to-greater-tree/description/

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

function convertBST(root: TreeNode | null): TreeNode | null {
    const S:TreeNode[] = [];
    let curr:TreeNode | null = root;
    let total:number = 0;
    while(S.length > 0 || curr){
        while(curr){
            S.push(curr)
            curr = curr.right;
        }
        curr = S.pop()!;
        total += curr.val;
        curr.val = total;
        curr = curr.left;


    }


    return root
};