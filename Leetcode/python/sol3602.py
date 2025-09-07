# https://leetcode.com/problems/hexadecimal-and-hexatrigesimal-conversion/solutions/7165684/separation-concerns-by-antoniojsp-aivi/
class Solution:
    def convert_to(self, n :int, base :int) -> str:
        '''
        Convert number from decimal to whatever base requested
        n: integer
        return: string
        '''
        chars = string.ascii_uppercase # list with all uppercase chars
        digits = []
        while 0 < n:
            if ( n %base) > 9: # get modulo of n by base and add result
                letter = chars[( n %base) - 10]
                digits.append(letter)
            else:
                digits.append(str( n %base))
            n = n// base  # divide n for next iteration
        return "".join(digits[::-1])  # invert result and join into a string (more efficient than adding string)

    def concatHex36(self, n: int) -> str:
        if n == 0:  # if n is zero, directly return 0
            return "0"
        return self.convert_to(n ** 2, 16) + self.convert_to(n ** 3, 36)

