# https://leetcode.com/problems/move-zeroes/
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return nums
        pos = 0
        for i, j in enumerate(nums):
            if j != 0:
                nums[pos] = j
                pos+=1

        for i in range(pos, len(nums)):
            nums[i] = 0




