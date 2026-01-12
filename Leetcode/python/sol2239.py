# https://leetcode.com/problems/find-closest-number-to-zero/description/
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        gap = abs(nums[0])  # initial gap and result, first value of array
        result = nums[0]
        for i in nums[1:]:
            distance = abs(i)
            if distance < gap:  # if distance if less of currenet gap, update
                gap = distance
                result = i
            elif distance == gap:  # if distance == gap, update only result with the max value
                result = max(result, i)
        return result
