# https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/description/

class Solution:
    def freqAlphabets(self, s: str) -> str:

        rslt = []
        i = len(s) - 1
        while i >= 0:
            if s[i] == "#":
                rslt.append(chr(int(s[i-2] + s[i-1])+96))
                i-=3
            else:
                rslt.append(chr(int(s[i])+96))
                i-=1

        return "".join(rslt[::-1])
