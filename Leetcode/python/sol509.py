# https://leetcode.com/problems/fibonacci-number/
class Solution:
    # @lru_cache
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fib( n -1) + self.fib( n -2)


class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        dp = [0]*(n)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n):
            dp[i] = dp[i-2] + dp[i-1]
        return dp[-1]