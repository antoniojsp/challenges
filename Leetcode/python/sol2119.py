
# https://leetcode.com/problems/a-number-after-a-double-reversal/description/
class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        if num % 10 == 0 and num != 0:
            return False
        return True