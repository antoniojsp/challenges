
# https://leetcode.com/problems/smallest-divisible-digit-product-i/


from itertools import accumulate
class Solution:
    def multiply_digits(self, num:int) -> int:
        result = 1
        while 0 < num:
            result*=num%10
            if result == 0:
                return 0
            num//=10
        return result

    def smallestNumber(self, n: int, t: int) -> int:
        while self.multiply_digits(n)%t != 0:
            n+=1
        return n



