# https://leetcode.com/problems/largest-odd-number-in-string/description/

class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num) - 1, -1, -1):  # check right to left, stop when first odd digit is found
            if int(num[i]) % 2 != 0:
                return num[:i + 1]  # return the number form from 0 to first odd num from the right
        return ""  # if none odd value, return empty string


