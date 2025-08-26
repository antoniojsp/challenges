# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# from typing import Optional
#
#
# class Solution:
#     def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
#         S = [(root, 0)]
#         result = 0
#         while S:
#             node, current= S.pop()
#             current = current * 2 + node.val
#             if not node.right and not node.left:
#                 result+=current
#
#             if node.right:
#                 S.append((node.right, current))
#             if node.left:
#                 S.append((node.left, current))
#
#
#         return result



binary = "1001011"
result = 0
for i in binary:
    result = result*2+int(i)
print(result)

