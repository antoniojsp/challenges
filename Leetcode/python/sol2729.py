# https://leetcode.com/problems/check-if-the-number-is-fascinating/description/
class Solution:
    def isFascinating(self, n: int) -> bool:
        candidate = "".join(str(( i +1 ) *n) for i in range(3)) # create
        if "0" in candidate:
            return False
        return len(set(candidate)) == 9 and len(candidate) == 9
