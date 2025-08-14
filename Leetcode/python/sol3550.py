# https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/description/
class Solution:
    def sum_digits(self, num):
        rslt = 0
        while 0 < num:
            rslt+=num %10
            num//=10
        return rslt

    def smallestIndex(self, nums: List[int]) -> int:
        for i, val in enumerate(nums):
            if i == self.sum_digits(val):
                return i
        return -1


