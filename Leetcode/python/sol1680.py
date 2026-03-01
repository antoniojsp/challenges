
#  https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/description/?envType=daily-question&envId=2026-02-28


class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10**9 + 7
        res = 0
        for i in range(1, n+1):
            length = floor(log2(i)) + 1
            res = ((res << length) + i)%MOD
        return res


