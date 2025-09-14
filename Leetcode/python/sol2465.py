# https://leetcode.com/problems/number-of-distinct-averages/description/
class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort() # sort array so start is the min and the end the max
        averages = set() # store the sums in a set to find the unique values
        start = 0
        end = len(nums) - 1

        while start < end:
            averages.add((nums[start ] +nums[end]) ) # no need to divide since all the process sum 2 values.
            start+=1
            end-=1
        return len(averages)
