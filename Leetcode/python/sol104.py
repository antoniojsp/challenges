# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        Q = [(root, 1)]
        max_depth = Q[-1][1]
        while Q:
            node, depth = Q.pop(0)
            max_depth = max(max_depth, depth)
            if node and node.left:
                Q.append((node.left, depth +1))
            if node and node.right:
                Q.append((node.right, depth +1))

        return max_depth
