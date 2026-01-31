



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

function isBalanced(root: TreeNode | null): boolean {
    if (!root){
        return true;
    }
    const S:[TreeNode | null, boolean][] = [[root, false]];
    const heightMap = new Map<TreeNode | null, number>();
    while(0 < S.length){
        const [node, visited] = S.pop();
        if(!node){
            continue;
        }

        if (!visited){
            S.push([node, true])//processed
            S.push([node.left, false])
            S.push([node.right, false])
        }else{
            let l_height = heightMap.get(node.left) ?? 0;
            let r_height = heightMap.get(node.right) ?? 0;
            if(Math.abs(l_height - r_height) > 1){
                return false;
            }
            heightMap.set(node, 1 + Math.max(l_height,r_height ))
        }
    }
    return true;
};





function isBalanced(root: TreeNode | null): boolean {
    if (!root){
        return true;
    }

    const checkHeight = (node) => {
        if (!node){
            return 0;
        }
        let leftHeight = checkHeight(node.left)
        if (leftHeight == -1){
            return -1;
        }

        let rightHeight = checkHeight(node.right);
        if (rightHeight == -1){
            return -1
        }

        if(Math.abs(rightHeight - leftHeight) > 1){
            return -1;
        }

        return 1 + Math.max(leftHeight, rightHeight)
    }

    return checkHeight(root) != -1;
}