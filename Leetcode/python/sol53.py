# https://leetcode.com/problems/maximum-subarray/
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        max_endin = nums[0]
        max_current = nums[0]

        for i in range(1, len(nums)):
            max_ending = max(nums[i], max_ending + nums[i])
            max_current = max(max_ending, max_current)

        return max_current
