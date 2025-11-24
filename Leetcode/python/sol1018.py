# https://leetcode.com/problems/binary-prefix-divisible-by-5/?envType=daily-question&envId=2025-11-24

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        result = []
        answer = 0
        for i, j in enumerate(nums):
            answer *= 2
            answer += j
            result.append(answer % 5 == 0)
        return result
