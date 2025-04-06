#  https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit :int = 0
        min_price :int = float("inf")
        for i in prices:
            if min_price > i:
                min_price = i
            else:
                max_profit = max(max_profit, i - min_price)
        return max_profit




