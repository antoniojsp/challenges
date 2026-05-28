# https://leetcode.com/problems/concatenate-array-with-reverse/description/
class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        res = [0 ] *(len(nums ) *2)
        start = 0
        end = len(res ) -1
        for i in range(len(nums)):
            res[start] = nums[i]
            start+=1
            res[end] = nums[i]
            end-=1
        return res
