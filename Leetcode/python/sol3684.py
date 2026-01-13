# https://leetcode.com/problems/maximize-sum-of-at-most-k-distinct-elements/?envType=problem-list-v2&envId=greedy

class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        uniques = sorted(list(set(nums)), reverse=True)  # inputs less than 100, if more, use heapq
        return uniques[:k]

