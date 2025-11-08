# https://leetcode.com/problems/remove-zeros-in-decimal-representation/description/



class Solution:
    def str_to_int(self, nums:list) -> int:
        rslt = 0
        for num in nums:
            rslt = rslt*10+int(num)
        return rslt

    def removeZeros(self, n: int) -> int:
        # number = list(filter(lambda x: x!="0", list(str(n))))
        # return self.str_to_int(number)
        return int("".join(filter(lambda x: x!="0", list(str(n)))))
