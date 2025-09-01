
# https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/

class Solution:
    def highest_power(self, n:int) -> int:
        '''
        Highest power that is lower than n (if power is greater than n, then there is no way that the sum of powers return n)
        '''
        power = 0
        while 3**power <= n:
            power+=1
        return power

    def checkPowersOfThree(self, n: int) -> bool:
        power = self.highest_power(n) # gets the highest power to use as starting point to calculate
        for i in range(power, -1, -1):
            three_power = 3**i
            if three_power <= n:
                n-=three_power
        return n == 0
