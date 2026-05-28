# https://leetcode.com/problems/check-adjacent-digit-differences/submissions/2015411513/


class Solution:
    def isAdjacentDiffAtMostTwo(self, s: str) -> bool:
        for i in range(len(s)-1):
            if abs(int(s[i]) - int(s[i+1])) > 2:
                return False
        return True