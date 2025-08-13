# https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/description/
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n_operations = 0
        for i in range(1, len(nums)):
            if nums[ i -1] >= nums[i]:
                min_next = nums[ i -1] + 1
                n_operations += min_next - nums[i]
                nums[i] = min_next
        return n_operations


