
# https://leetcode.com/problems/find-the-key-of-the-numbers/description/


class Solution:
    def adding_leading_zeros(self, num:int) -> str:
        num_str:str = str(num)
        zeros:int = 4 - len(num_str)
        return "0" * zeros + num_str

    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        values = [self.adding_leading_zeros(num) for num in [num1, num2, num3]]
        rslt = 0
        for i in range(4):
            mininum = float("inf")
            for val in values:
                mininum = min(mininum, int(val[i]))
            rslt+= mininum*(10**(4-1-i))
            i+=1
        return rslt
