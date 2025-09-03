# https://leetcode.com/problems/path-sum/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def helper(node, current):
            if not node: # if None
                return False

            current += node.val

            if not (node.left or node.right):  # look for leavea
                return current == targetSum

            return helper(node.left, current) or helper(node.right, current)

        return helper(root, 0)






