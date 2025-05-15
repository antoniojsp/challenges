#  https://leetcode.com/problems/evaluate-boolean-binary-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def evaluateTree(self, root: Optional[TreeNode]) -> bool:
#         if not root.left or not root.right:
#             return root.val == 1
#         if root.val == 2:
#             return self.evaluateTree(root.left) or self.evaluateTree(root.right)
#         elif root.val == 3:
#             return self.evaluateTree(root.left) and self.evaluateTree(root.right)

a = (1,2,3)
b = (2,1,3)
print(a == b)
print([0,0,1] == [0,1,0])
a = [[0,0,1], [0,0,1], [0,1,1]]
print([1,0,1] in a)