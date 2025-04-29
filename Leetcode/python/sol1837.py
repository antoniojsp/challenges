# https://leetcode.com/problems/sum-of-digits-in-base-k/description/
class Integer:
    def __init__(self, value):
        self.num = value

    def convert_to_base(self, k):
        rslt = 0
        i = 0
        original = self.num
        while 0 < original:
            rslt+= original%k * (10**i)
            i+=1
            original = original//k
        return rslt

    def add_digits_result(self, base)->int:
        value = self.convert_to_base(base)
        rslt = 0
        while 0 < value:
            rslt+=value%10
            value//=10
        return rslt

class Solution:
    def sumBase(self, n: int, k: int) -> int:
        value = Integer(n)
        return value.add_digits_result(k)



