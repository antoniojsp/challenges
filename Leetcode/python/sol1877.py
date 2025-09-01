# https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        max_sum = -1

        for i in range(len(nums )//2):
            max_sum = max(max_sum, nums[i ] +nums[len(nums ) - 1 -i])

        return max_sum


