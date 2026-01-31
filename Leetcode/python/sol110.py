# https://leetcode.com/problems/balanced-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(node):
            if not node:
                return 0
            left = helper(node.left)
            if left == -1:
                return -1
            right = helper(node.right)
            if right == -1:
                return -1
            if abs(left-right) > 1:
                return -1

            return 1 + max(left, right)

        return helper(root) != -1


        # if not root:
        #     return True

        # S = [(root, False)]
        # heights = {}
        # while S:
        #     node, visited = S.pop()
        #     if not node:
        #         continue
        #     if not visited:
        #         # if not visited, then add the node, and child to the stack
        #         S.append((node, True))
        #         S.append((node.left, False))
        #         S.append((node.right, False))
        #     else:
        #         l_height = heights.get(node.left, 0)
        #         r_height = heights.get(node.right, 0)
        #         if abs(l_height-r_height) > 1:
        #             return False
        #         heights[node] = 1+max(l_height,r_height)
        # return True

