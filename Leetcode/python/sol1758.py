
# https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/description/

class Solution:
    def generate_bin(self, length, startwith):
        flag = startwith == "1"
        rslt = []
        for i in range(length):
            if flag:
                rslt.append("1")
            else:
                rslt.append("0")
            flag=not flag
        return rslt

    def minOperations(self, s: str) -> int:
        zero = self.generate_bin(len(s), "0")
        one = self.generate_bin(len(s), "1")
        rslt_zero = 0
        rslt_one = 0
        for i in range(len(s)):
            if zero[i] != s[i]:
                rslt_zero += 1
            if one[i] != s[i]:
                rslt_one +=1

        return min(rslt_zero, rslt_one)
