# https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i/description/

class Solution:
    def hasSameDigits(self, s: str) -> bool:
        num = list(map(int, s))  # start by converting the string num to list of int
        while len(num) > 2:
            rslt = []  # temp list
            for i in range(1, len(num)):
                rslt.append((num[i - 1] + num[i]) % 10)  # sum and get modulo 10
            num = rslt  # update num
        return num[0] == num[1]  # check 2 digits and equal

