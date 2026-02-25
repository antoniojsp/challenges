
# https://leetcode.com/problems/longest-harmonious-subsequence/description/

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count = Counter(nums)
        longest_sub = 0
        for i, j in count.items():
            if i + 1 in count:
                longest_sub = max(longest_sub, count[i] + count[i+1])

        return longest_sub