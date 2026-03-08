//https://leetcode.com/problems/merge-two-binary-trees/
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

function mergeTrees(root1: TreeNode | null, root2: TreeNode | null): TreeNode | null {
    if (!root1){
        return root2;
    }
    const stack:[TreeNode, TreeNode][] = [[root1, root2]];
    while(stack.length > 0){
        const [node1, node2] = stack.pop();
        if (!node2){
            continue;
        }
        node1.val+=node2.val;
        if(node1.left && node2.left){
            stack.push([node1.left, node2.left]);
        }else if(!node1.left){
            node1.left = node2.left;
        }

        if(node1.right && node2.right){
            stack.push([node1.right, node2.right]);
        }else if(!node1.right){
            node1.right = node2.right;
        }
    }
    return root1;
};

