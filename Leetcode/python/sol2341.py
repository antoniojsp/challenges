
# https://leetcode.com/problems/maximum-number-of-pairs-in-array/solutions/7107979/pythonic-and-easy-to-understand-by-anton-9pak/

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        count = {}
        for i in nums:
            count[i] = count.get(i, 0)+1 # count freq elements in nums
        pair = sum(i//2 for i in count.values())
        single = sum(i%2 for i in count.values())
        return [pair, single]
