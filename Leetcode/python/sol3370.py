
# https://leetcode.com/problems/smallest-number-with-all-set-bits/description/
class Solution:
    def binary(self, num:int) -> list[int]:
        rslt = []
        while 0 < num:
            rslt.append(num%2)
            num//=2
        return rslt
    def smallestNumber(self, n: int) -> int:
        length = len(self.binary(n))
        rslt = 0
        for i in range(length):
            rslt+= 2**i
        return rslt
