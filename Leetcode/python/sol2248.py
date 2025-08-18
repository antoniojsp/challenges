# https://leetcode.com/problems/intersection-of-multiple-arrays/description/

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        counter = set(nums[0])
        for i in nums[1:]:
            counter &= set(i)
        return sorted(list(counter))