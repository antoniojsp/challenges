
//https://leetcode.com/problems/binary-tree-level-order-traversal/description/

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

function levelOrder(root: TreeNode | null): number[][] {
    if(!root){
        return [];
    }
    const Q:[TreeNode | null, number][] = [[root, 0]];
    const mapa = new Map();

    while(Q.length > 0){
        const popped: [TreeNode | null, number] | undefined = Q.shift();
        if(!popped){
            continue;
        }

        const [node, level] = popped;
        if(node != null){
            console.log(node.val, level)
            if(!(level in mapa)){
                mapa[level] = [];
            }
            mapa[level].push(node.val)

            if(node.left){
                Q.push([node.left, level + 1])
            }
            if(node.right){
                Q.push([node.right, level + 1])
            }
        }
    }

    return Object.values(mapa);
};