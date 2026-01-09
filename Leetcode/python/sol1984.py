# https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/description/
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        nums.sort()
        result = float('inf')
        for i in range(len(nums ) - k +1):
            result = min(result, nums[ i + k -1] - nums[i])
        return result

