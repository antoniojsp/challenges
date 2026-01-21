# https://leetcode.com/problems/largest-even-number/description/


class Solution:
    def largestEven(self, s: str) -> str:
        end = len(s)
        for i in range(len(s)-1,-1,-1):
            if s[i] == "1":
                end = i
            else:
                break
        return s[:end]