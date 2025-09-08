# https://leetcode.com/problems/minimum-sum-of-mountain-triplets-i/
class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        min_sum_triple = float('inf')
        for i in range(1, len(nums ) -1):
            current = nums[i]
            min_left = float('inf')
            for j in range(0, i):
                if nums[j] < current:
                    min_left = min(min_left, nums[j])
            min_right = float('inf')
            for k in range(len(nums ) -1, i, -1):
                if current > nums[k]:
                    min_right = min(min_right, nums[k])

            if not isinf(min_left) and not isinf(min_right):
                min_sum_triple = min(min_left + current + min_right, min_sum_triple)
        return -1 if min_sum_triple == float('inf') else min_sum_triple




