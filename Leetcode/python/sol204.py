# https://leetcode.com/problems/count-primes/description/

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0

        primes = [1]*(n+1)
        primes[0], primes[1] = 0, 0
        for i in range(2, int(sqrt(n))+1):
            if primes[i] == 1:
                for j in range(i*i, n+1, i):
                    primes[j] = 0

        return sum(primes[:-1])