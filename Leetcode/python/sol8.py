# https://leetcode.com/problems/string-to-integer-atoi/
INT_MAX = 2** 31 - 1
INT_MIN = -2 ** 31


class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()  # clean the leading empty spaces
        if not s:
            return 0
        result = ""
        sign = 1  # default positive, if there is a "-", then set sign to -1
        i = 0
        if s[0] == "+":  # if first char after cleaning has sign, add sign and move one index
            i += 1
        elif s[0] == "-":
            sign = -1
            i += 1

        while i < len(s) and s[i].isdigit():  # keep going and adding to result
            result += s[i]
            i += 1

        if result in ["", "+", "-"]:  # if result is only "+", "-" or empty, return zero
            return 0

        rslt = sign * int(result)  # add the sign to the result

        if rslt > INT_MAX:  # check if the value is om range of 32 bits
            rslt = INT_MAX
        elif rslt < INT_MIN:
            rslt = INT_MIN
        return rslt


