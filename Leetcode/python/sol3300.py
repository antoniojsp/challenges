# https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/description/


class Solution:
    def sum_digits(self, nums: int) -> int:
        rslt = 0
        while 1 <= nums:
            rslt+=nums%10
            nums//=10
        return rslt
    def minElement(self, nums: List[int]) -> int:
        return min(self.sum_digits(i) for i in nums)