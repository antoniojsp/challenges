# https://leetcode.com/problems/calculate-amount-paid-in-taxes/description/
class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        total = 0
        so_far = 0
        for limit, porcentage in brackets:
            if limit <= income:
                total += (limit - so_far ) *(porcentage /100)
                so_far = limit
            else:
                remainder = income - so_far
                total += remainder *(porcentage /100)
                break

        return total


