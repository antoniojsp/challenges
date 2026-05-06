
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        suma = 0
        def traverse(node):
            nonlocal suma
            if not node:
                return None
            traverse(node.right)
            suma+=node.val
            node.val = suma
            traverse(node.left)
        traverse(root)
        return root
