#  https://leetcode.com/problems/replace-all-digits-with-characters/description/
class Solution:
    def shift(self, character: str, shift: chr):
        return chr(ord(character ) +shift)

    def replaceDigits(self, s: str) -> str:
        rslt = list(s)
        for i in range(1, len(s), 2):
            rslt[i] = self.shift(s[ i -1], int(s[i]))

        return "".join(rslt)

