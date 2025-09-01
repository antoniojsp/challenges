# https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/description/

class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        length = len(nums)
        for i in range(length):
            if nums[i] > 9: # if num has one digit, then inverted is the same
                inverted = int(str(nums[i])[::-1])
                nums.append(inverted)
        return len(set(nums))