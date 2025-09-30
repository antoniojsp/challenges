# https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/description/?envType=problem-list-v2&envId=enumeration

from itertools import combinations

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        result = defaultdict(int)
        for i in range(1, len(nums)+1):
            for subset in combinations(nums, i):
                result[reduce(lambda x, y: x | y, subset)]+=1

        return max(result.values())