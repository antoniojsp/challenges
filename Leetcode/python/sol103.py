

# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = deque()
        def helper(node:TreeNode, level:int):
            if not node:
                return

            if level == len(res):
                res.append(deque())

            if level%2 == 0:
                res[level].append(node.val)
            else:
                res[level].appendleft(node.val)

            helper(node.left, level+1)
            helper(node.right, level+1)

        helper(root, 0)
        return [list(i) for i in res]