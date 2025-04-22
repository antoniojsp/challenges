# https://leetcode.com/problems/squares-of-a-sorted-array/description/
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        rslt = [0 ] *len(nums)
        L = 0
        R = len(nums ) -1

        for i in range(len(nums ) -1, -1 ,-1):
            if abs(nums[L]) > abs(nums[R]):
                val = nums[L]
                L+=1
            else:
                val = nums[R]
                R-=1
            rslt[i] = val** 2

        return rslt


