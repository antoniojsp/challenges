
# https://leetcode.com/problems/self-dividing-numbers/description/
class Solution:
    def digits(self, num:int) -> list:
        rslt = []
        while num >= 1:
            rslt.append(num%10)
            num//=10
        return rslt

    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        rslt = []
        for val in range(left, right+1):
            add = True
            for digit in self.digits(val):
                if digit == 0:
                    add = False
                    break
                if val%digit != 0:
                    add = False
                    break
            if add:
                rslt.append(val)
        return rslt
