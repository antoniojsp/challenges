# https://leetcode.com/problems/plus-one/submissions/1658486566/
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits ) -1, -1 ,-1):
            if digits[i ] +1 <= 9:
                digits[i ]+ =1
                return digits
            else:
                digits[i] = 0 # since you are adding only 1

        return [1] + digits
