# https://leetcode.com/problems/running-sum-of-1d-array/
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for idx, val in enumerate(nums[1:], start=1):
            nums[idx] = nums[id x -1] + val

        return nums



