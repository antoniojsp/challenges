# https://leetcode.com/problems/four-divisors/description/?envType=daily-question&envId=2026-01-04
from math import sqrt
from typing import List


class Solution:
    def num_divisors(self, num )-> set:
        divisor = set()
        for i in range(1, int(sqrt(num) ) +1):
            if num%i == 0:
                divisor.add(i)
                divisor.add(num//i)
            if len(divisor) > 4:
                break
        return divisor

    def sumFourDivisors(self, nums: List[int]) -> int:
        result = 0
        for i in nums:
            divisors = self.num_divisors(i)
            if len(divisors) == 4:
                result += sum(divisors)

        return result

