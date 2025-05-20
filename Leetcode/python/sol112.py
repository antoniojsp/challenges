# //https://leetcode.com/problems/path-sum/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if not root:
            return False

        Q = [(root, root.val)]

        while Q:
            node, suma = Q.pop()
            if node.left is None and node.right is None and suma == targetSum:
                return True

            if node.left:
                Q.append((node.left, suma+node.left.val))
            if node.right:
                Q.append((node.right, suma+node.right.val))


        return False




