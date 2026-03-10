
# https://leetcode.com/problems/perfect-squares/

class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i*i for i in range(1, int(sqrt(n) + 1))]
        memo = {}
        def helper(val):
            if val in memo:
                return memo[val]
            if val == 0:
                return 0
            if val < 0:
                return -1
            minimum = float('inf')
            for i in squares:
                res = helper(val - i)
                if res != -1:
                    minimum = min(minimum, res + 1)
            memo[val] = minimum
            return memo[val]
        return helper(n)
