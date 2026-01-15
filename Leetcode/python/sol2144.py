# https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/description/?envType=problem-list-v2&envId=greedy


class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        if len(cost) < 3:
            return sum(cost)
        cost.sort(reverse=True)
        result = sum(cost)
        for i in range(2, len(cost), 3):
            result -= cost[i]
        return result
