# https://leetcode.com/problems/find-the-sum-of-encrypted-integers/description/
class Solution:

    def encrypt(self, num :int) -> int:
        max_digit :int = 0
        count :int = 0
        while 0 < num:
            max_digit = max(max_digit, num %10)
            num//=10
            count+=1

        rslt :int = 0
        for i in range(count):
            rslt+=max_digit *(10**i)

        return rslt


    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        rslt :int = 0
        for i in nums:
            rslt+=self.encrypt(i)

        return rslt
