
# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-iii/solutions/7499162/simple-by-antoniojsp-5w9y/


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        max_val = max(nums)
        result = 0
        for i in nums:
            result+=max_val - i
        return result