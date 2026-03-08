
# https://leetcode.com/problems/increasing-order-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        temp = TreeNode(val=-1)
        dummy = temp
        def helper(node):
            nonlocal dummy
            if not node:
                return
            helper(node.left)
            dummy.right = TreeNode(val=node.val)
            # node.left = None
            # dummy.right = node
            dummy = dummy.right
            helper(node.right)
        helper(root)
        return temp.right