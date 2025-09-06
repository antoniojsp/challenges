

# https://leetcode.com/problems/find-triangular-sum-of-an-array/description/

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while  1 < len(nums):
            temp = []
            for i in range(len(nums)-1):
                temp.append((nums[i]+nums[i+1])%10)
            nums = temp
        return nums[0]

