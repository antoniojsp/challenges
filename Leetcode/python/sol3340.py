# https://leetcode.com/problems/check-balanced-string/description/

class Solution:
    def isBalanced(self, num: str) -> bool:
        suma: int = 0
        for i, j in enumerate(num):
            if i % 2 == 0:
                suma += int(j)
            else:
                suma -= int(j)
        return not suma
