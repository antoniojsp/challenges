
# https://leetcode.com/problems/sum-of-variable-length-subarrays/description/

class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        suma = 0
        for idx, val in enumerate(nums):
            start = max(0, idx - val + 1)
            suma+=sum(nums[start:idx+1])
        return suma


class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        suma = 0
        prefix = [0]*(len(nums)+1)
        for i in range(0, len(nums)):
            prefix[i+1] = prefix[i] + nums[i]

        for i in range(0, len(nums)):
            start = max(0, i-nums[i])
            suma += prefix[i+1]-prefix[start]

        return suma


