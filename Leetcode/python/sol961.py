
# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        seen = set()
        rslt = -1
        for i in nums:
            if i in seen:
                rslt = i
                break
            seen.add(i)
        return rslt
