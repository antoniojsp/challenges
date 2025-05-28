# https://leetcode.com/problems/maximum-count-of-positive-integer-and-negative-integer/

class Solution:

    def first_positive(self, nums):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] > 0:
                right = mid - 1
            else:
                left =  mid + 1
        return left

    def first_negative(self, nums):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] < 0:
                left = mid + 1
            else:
                right =  mid - 1
        return right

    def maximumCount(self, nums: List[int]) -> int:
        pos = self.first_positive(nums)
        neg = self.first_negative(nums)

        return max(neg+1, len(nums)-pos)