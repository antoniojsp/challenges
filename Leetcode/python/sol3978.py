# https://leetcode.com/problems/unique-middle-element/description/


class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        count = Counter(nums)
        mid = len(nums)//2
        return count[nums[mid]] == 1
