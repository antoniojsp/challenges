# https://leetcode.com/problems/minimum-distance-between-bst-nodes/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        prev = None
        min_difference = float('inf')
        def helper(node):
            nonlocal prev, min_difference
            if not node:
                return
            helper(node.left)

            if prev is not None:
                min_difference = min(node.val - prev, min_difference)
            prev = node.val

            helper(node.right)

        helper(root)
        return min_difference


