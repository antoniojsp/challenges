# # https://leetcode.com/problems/sort-colors/description/
#
# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         freq = {0:0, 1:0, 2:0}
#         for i in nums:
#             freq[i] += 1
#
#         i = 0
#         while i < len(nums):
#             if i < freq[0]:
#                 nums[i] = 0
#             elif i < freq[0] + freq[1]:
#                 nums[i] = 1
#             else:
#                 nums[i] = 2
#             i+=1
#
#
# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         i = 1
#         while i < len(nums):
#             current = i
#             while 0 < current and nums[current-1] > nums[current]:
#                 nums[current], nums[current-1] = nums[current-1], nums[current]
#                 current-=1
#             i+=1



