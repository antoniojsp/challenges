# https://leetcode.com/problems/combination-sum-iv/
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}
        def helper(val):
            if val in memo:
                return memo[val]
            if val == 0:
                return 1
            if val < 0:
                return 0
            count = 0
            for i in nums:
                count += helper(val - i)
            memo[val] = count
            return count
        return helper(target)
