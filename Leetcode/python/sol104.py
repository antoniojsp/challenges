# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        Q = deque([(root, 1)])
        max_depth = 0
        while Q:
            node, depth = Q.popleft()
            max_depth = max(max_depth, depth)
            if node.left:
                Q.append((node.left, depth +1))
            if node.right:
                Q.append((node.right, depth +1))

        return max_depth
#
# from collections import deque
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0
#         left = self.maxDepth(root.left)
#         right = self.maxDepth(root.right)
#         return 1 + max(left, right)