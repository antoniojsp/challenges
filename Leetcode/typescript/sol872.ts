

// https://leetcode.com/problems/leaf-similar-trees/description/



class TreeNode {
    val: number;
    left: TreeNode | null;
    right: TreeNode | null;

    constructor(
        val: number = 0,
        left: TreeNode | null = null,
        right: TreeNode | null = null
    ) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

const leavesEnds = (root:TreeNode | null) => {
    if(!root){
        return [];
    }
    const S:TreeNode[] = [root]
    let result:number[] = [];
    while(S.length != 0){
        const node:TreeNode = S.pop()!;
        if(!node.left && !node.right){
            result.push(node.val);
        }

        if(node.left){
            S.push(node.left);
        }
        if(node.right){
            S.push(node.right);
        }
    }
    return result;
}

function leafSimilar(root1: TreeNode | null, root2: TreeNode | null): boolean {
    const ends1:number[] = leavesEnds(root1);
    const ends2:number[] = leavesEnds(root2);

    if(ends1.length != ends2.length){
        return false;
    }

    for(let i = 0; i < ends1.length; i++){
        if(ends1[i] !== ends2[i]){
            return false;
        }
    }

    return true;
};