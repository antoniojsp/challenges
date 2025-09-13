
class Solution:
    def product(self, n :int )->int:
        """
        Multiply the digits in n
        """
        result = 1
        while 0 < n:
            result*=(n%10)
            n//=10
        return result

    def digit_sum(self, n:int)->int:
        '''
        Sum of the digits of n
        '''

        result = 0
        while 0 < n:
            result+=(n%10)
            n//=10
        return result

    def checkDivisibility(self, n: int) -> bool:
        '''
        if n is zero, it can produce an error "dividing by zero", but since the
        constraints say that the values start at 1, there is no need to check for n = 0
        '''
        return n%(self.product(n)+self.digit_sum(n)) == 0
