# https://leetcode.com/problems/validate-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        Q = [(root, -float("inf"), float("inf"))]
        while Q:
            node, min_val, max_val = Q.pop()
            if not (min_val < node.val < max_val):
                return False
            if node.left:
                Q.append((node.left, min_val, node.val))
            if node.right:
                Q.append((node.right, node.val, max_val))
        return True



class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, min, max):
            if not node:
                return True
            if (min is not None) and (node.val <= min) \
                or \
               (max is not None) and (node.val >= max):
                return False

            return helper(node.left, min, node.val) and helper(node.right, node.val, max)
        return helper(root, None, None)