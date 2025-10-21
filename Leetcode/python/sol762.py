#https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/description/
class Solution:
    def isPrime(self, value):
        if value < 2: return False
        if value == 2: return True
        if valu e %2 == 0: return False
        count = 0
        for i in range(3, int(valu e* *0.5 ) +1, 2):
            if valu e % i= =0:
                return False
        return True

    def countPrimeSetBits(self, left: int, right: int) -> int:
        count = 0
        for i in range(left, righ t +1):
            if self.isPrime(bin(i).count("1")):
                coun t+ =1
        return count
