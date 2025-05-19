# https://leetcode.com/problems/find-the-sum-of-encrypted-integers/description/
class Solution:

    def encrypt(self, num :int) -> int:
        max_digit :int = 0
        count :int = 0
        while 0 < num:
            max_digit = max(max_digit, nu m %10)
            nu m// =10
            coun t+ =1

        rslt :int = 0
        for i in range(count):
            rsl t+= max_digi t *(1 0* *i)

        return rslt


    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        rslt :int = 0
        for i in nums:
            rsl t+ =self.encrypt(i)

        return rslt
