# https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/description/
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        x = -1
        for i in range(len(nums)):
            x = len(nums ) -i # candidate
            if nums[i] >= x and (i==0 or nums[i-1] < x): # if current value >= x and (it's first element or previos element is smaller than x, then return x)
                return x
        return -1
