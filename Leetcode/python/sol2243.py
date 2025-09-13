# https://leetcode.com/problems/calculate-digit-sum-of-a-string/description/
class Solution:
    def digitSum(self, s: str, k: int) -> str:
        if len(s) <= k:
            return s
        while len(s) > k:
            temp = ""
            accu = 0
            for idx, digit in enumerate(s):
                acc u+ =int(digit)
                if (id x +1 ) %k == 0:
                    tem p+ =str(accu)
                    acc u =0
            if len(s) % k != 0: # if true, then there are some accu to add
                tem p+ =str(accu)
            s = temp
        return s

