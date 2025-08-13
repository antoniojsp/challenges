# https://leetcode.com/problems/array-partition/

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        pairs = []
        rslt = 0
        for i in range(0, len(nums), 2):
            rslt += nums[i]

        return rslt
