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





class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def helper(val, memo=None):
            if memo is None:
                memo = {}
            if val == 0:
                return 0
            if val < 0:
                return -1
            if val in memo:
                return memo[val]
            minimum = float("inf")
            for i in coins:
                res = helper(val-i, memo)
                if res != -1: # if return -1. then it means it added too many coins
                    minimum = min(minimum, 1 + res)
            memo[val] = -1 if minimum == float('inf') else minimum # if no combination found, then store -1
            return memo[val]
        return helper(amount)