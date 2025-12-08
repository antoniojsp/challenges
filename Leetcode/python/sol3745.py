# https://leetcode.com/problems/maximize-expression-of-three-elements/description/

class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:
        max1 = max2 = float("-inf")
        min1 = float("inf")
        for i in nums:
            if max1 < i:
                max2 = max1
                max1 = i
            elif i > max2:
                max2 = i
            if i < min1:
                min1 = i
        return max1 + max2 - min1
