# https://leetcode.com/problems/coin-change/description/


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        for quantity in range(1, amount+1):
            for coin in coins:
                need = quantity - coin
                if need >= 0:
                    dp[quantity] = min(dp[quantity], dp[need]+1) # plus 1 adding the current coin
        return dp[amount] if dp[amount] != float('inf') else -1
