# https://leetcode.com/problems/find-closest-number-to-zero/description/
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        gap = abs(nums[0])
        result = nums[0]
        for i in nums[1:]:
            if abs(i) < gap:
                gap = abs(i)
                result = i
            elif abs(i) ==  gap:
                result = max(result, i)
        return result
