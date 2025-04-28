# https://leetcode.com/problems/sum-of-unique-elements/description/

from collections import Counter
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        counting = Counter(nums)
        suma:int = 0
        for i, j in counting.items():
            if j == 1:
                suma+=i

        return suma