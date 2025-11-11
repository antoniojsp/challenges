# https://leetcode.com/problems/find-the-maximum-divisibility-score/
class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        bank = {}
        max_score = 0
        for j in set(divisors):
            bank[j] = 0
            for num in nums:
                if num % j == 0:
                    bank[j] += 1
            max_score = max(max_score, bank[j])
        rslt = [key for key, val in bank.items() if val == max_score]
        return min(rslt)
