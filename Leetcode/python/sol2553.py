# https://leetcode.com/problems/separate-the-digits-in-an-array/description/
class Solution:
    def separate(self ,num):
        digits = []
        while 1  <= num:
            temp = num %10
            num//=10
            digits.append(temp)
        return digits[::-1]

    def separateDigits(self, nums: List[int]) -> List[int]:
        rslt = []
        for i in nums:
            temp = self.separate(i)
            rslt.extend(temp)
        return rslt