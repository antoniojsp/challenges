# https://leetcode.com/problems/smallest-range-i/description/

class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        lowest = min(nums)
        highest = max(nums)
        '''
        diff = (highest-k) - (lowest + k)) // minimize the range of diff
        '''
        return (highest-k) - (lowest + k) if (highest-k) - (lowest + k) >=0 else 0