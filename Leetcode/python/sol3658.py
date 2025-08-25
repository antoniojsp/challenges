# https://leetcode.com/problems/gcd-of-odd-and-even-sums/description/

class Solution:
    def sum_odd_even(self, n:int)->(int, int):
        odd_sum, even_sum  = 0, 0
        for i in range(1, 2*n+1):
            if i%2 == 0:
                even_sum+=i
            else:
                odd_sum+=i
        return even_sum, odd_sum

    def gcdOfOddEvenSums(self, n: int) -> int:
        a, b = self.sum_odd_even(n)
        gcd = 1
        while b:
            a, b = b, a % b

        return a