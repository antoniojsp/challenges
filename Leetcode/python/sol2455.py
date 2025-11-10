# https://leetcode.com/problems/average-value-of-even-numbers-that-are-divisible-by-three/description/
class Solution:
    def averageValue(self, nums: List[int]) -> int:
        total = 0
        count = 0
        for num in nums:
            if num % 6 == 0:
                tota l+ =num
                coun t+ =1
        return tota l/ /count if count  else 0
