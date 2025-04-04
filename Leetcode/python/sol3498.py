
# https://leetcode.com/problems/reverse-degree-of-a-string/description/


class Solution:
    def reverseDegree(self, s: str) -> int:
        result = 0
        for i,j in enumerate(s, start=1):
            position_char = ord(j)-96
            reversal = 27 - position_char
            result += (reversal*i)

        return result