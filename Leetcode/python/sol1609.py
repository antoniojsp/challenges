


from collections import deque, defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def decreasing(self, nums):
        return all(nums[i] > nums[i+1] for i in range(len(nums)-1))

    def increasing(self, nums):
        return all(nums[i] < nums[i+1]for i in range(len(nums)-1))

    def all_odd(self, nums:list[int]) -> bool:
        return all(i%2!=0 for i in nums)

    def all_even(self, nums:list[int]) -> bool:
        return all(i%2==0 for i in nums)

    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        S = deque([(root, 0)])
        result = defaultdict(list)
        while S:
            node, level = S.popleft()
            if node:
                result[level].append(node.val)
                if node.left:
                    S.append((node.left, level+1))
                if node.right:
                    S.append((node.right, level+1))

        for l, arr in result.items():
            if l%2==0:
                if not self.all_odd(arr) or not self.increasing(arr):
                    return False
            else:
                if not self.all_even(arr) or not self.decreasing(arr):
                    return False

        return True