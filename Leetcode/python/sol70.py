# https://leetcode.com/problems/climbing-stairs/description/
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        prev1, prev2 = 1, 1
        for _ in range(n):
            prev1, prev2 = prev2, prev 2 +prev1

        return prev1




