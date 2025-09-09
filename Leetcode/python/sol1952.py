# https://leetcode.com/problems/three-divisors/


class Solution:
    def isThree(self, n: int) -> bool:
        count = 0
        for i in range(1, n+1):
            if n%i == 0:
                count+=1

        return count == 3



class Solution:
    def is_prime(self, n):
        primes = [True]*(n+1)
        primes[0] = False
        primes[1] = False
        for p in range(2, int(n**0.5)+1):
            if primes[p]:
                for i in range(p**2, n+1, p):
                    primes[i] = False
        return primes[n]

    def isThree(self, n: int) -> bool:
        '''
        perfect square of a primes has exactly 3 divisors
        '''
        if n <= 2:
            return False
        root = int(math.sqrt(n)) # get the roots
        if root**2 != n: # check if it's a perfect square
            return False
        return self.is_prime(int(root))
