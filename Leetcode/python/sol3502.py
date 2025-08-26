# https://leetcode.com/problems/minimum-cost-to-reach-every-position/
class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        lowest = cost[0]
        result = [lowest]
        for i in range(1 ,len(cost)):
            if cost[i] <= lowest:
                lowest = cost[i]
                result.append(lowest)
            else:
                result.append(lowest)
        return result
