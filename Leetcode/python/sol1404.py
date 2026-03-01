
# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/description/

class Solution:
    def binToDecimal(self, s) -> int:
        res = 0
        exp = 0
        for i in s[::-1]:
            # res = res * 2 + int(i)
            res += int(i)*2**exp
            exp+=1
        return res

    def numSteps(self, s: str) -> int:
        # decimal = self.binToDecimal(s)
        decimal = int(s, 2)
        count = 0
        while decimal > 1:
            count += 1
            if decimal % 2 == 0:
                decimal //= 2
            else:
                decimal +=1
        return count