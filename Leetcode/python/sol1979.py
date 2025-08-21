# https://leetcode.com/problems/find-greatest-common-divisor-of-array/description/
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        greatest = max(nums)
        lowest = min(nums)
        gcd = 1
        for i in range(lowest + 1, 0, -1):
            if greatest%i == 0 and lowest%i == 0:
                gcd = i
                break
        return gcd
