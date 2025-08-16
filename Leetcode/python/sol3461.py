# https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i/description/
class Solution:
    def hasSameDigits(self, s: str) -> bool:
        num = list(map(int, s))
        while len(num ) >2:
            rslt = []
            for i in range(1, len(num)):
                rslt.append((num[ i -1 ] +num[i] ) %10)
            num = rslt
        return num[0] == num[1]

