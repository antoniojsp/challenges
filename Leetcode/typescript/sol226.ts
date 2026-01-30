
// https://leetcode.com/problems/invert-binary-tree/description/

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

function invertTree(root: TreeNode | null): TreeNode | null {
    if(!root){
        return null;
    }
    const right = invertTree(root.right);
    const left = invertTree(root.left);
    root.right = left;
    root.left = right;
    return root;



    // const S:TreeNode[] = [root]
    // while(S.length > 0){
    //     let node:TreeNode = S.pop()
    //     if(node){
    //         [node.left, node.right] = [node.right, node.left]
    //         S.push(node.left)
    //         S.push(node.right)
    //     }
    // }
    // return root;
};