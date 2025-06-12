#  https://leetcode.com/problems/find-largest-value-in-each-tree-row/submissions/1661959947/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = {}
        def helper(node, level):
            if not node:
                return
            if level not in res:
                res[level] = node.val
            else:
                res[level] = max(res[level], node.val)
            helper(node.left, level + 1)
            helper(node.right, level + 1)
        helper(root, 0)
        return list(res.values())

