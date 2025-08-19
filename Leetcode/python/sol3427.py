
# https://leetcode.com/problems/sum-of-variable-length-subarrays/description/

class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        suma = 0
        for idx, val in enumerate(nums):
            start = max(0, idx - val)
            suma+=sum(nums[start:idx+1])
        return suma