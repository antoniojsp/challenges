
#  https://leetcode.com/problems/special-array-i/description/?envType=problem-list-v2&envId=array

class Solution:

    def even_or_odd(self, num):
        return "even" if num%2==0 else "odd"
    def isArraySpecial(self, nums: List[int]) -> bool:

        if len(nums) == 1:
            return True

        for i in range(1,len(nums)):
            if self.even_or_odd(nums[i-1]) == self.even_or_odd(nums[i]):
                return False

        return True