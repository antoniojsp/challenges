
# https://leetcode.com/problems/maximum-binary-tree/submissions/1751076863/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find_index_max(self, nums:List[int]) -> int:
        max_val_index = 0
        max_val = float('-inf')
        for idx, val in enumerate(nums):
            if max_val < val:
                max_val = val
                max_val_index = idx
        return max_val_index

    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(arr:List[int]):
            if not arr:
                return None
            max_i = self.find_index_max(arr)
            root = TreeNode(arr[max_i])
            root.left = helper(arr[:max_i])
            root.right = helper(arr[max_i+1:])
            return root

        return helper(nums)