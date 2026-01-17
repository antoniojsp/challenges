# https://leetcode.com/problems/absolute-difference-between-maximum-and-minimum-k-elements/description/
class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        if len(nums) == 1 or len(nums) == k:
            return 0
        nums.sort()
        return abs(sum(nums[:k]) - sum(nums[-k:]))
