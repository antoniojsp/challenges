# https://leetcode.com/problems/min-cost-climbing-stairs/
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0 ] *(len(cost ) +1)
        dp[0] = 0 # start from 0 or 1 step
        dp[1] = 0

        for i in range(2, len(dp)):
            dp[i] = min(dp[ i -1 ] +cost[ i -1] ,dp[ i -2 ] +cost[ i -2])

        return dp[-1]

