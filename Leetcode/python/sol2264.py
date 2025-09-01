# https://leetcode.com/problems/largest-3-same-digit-number-in-string/description/?envType=problem-list-v2&envId=string
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        current_max = float('-inf')
        rslt = ""
        for i in range(len(num ) -2):
            temp = num[i: i +3]
            if len(set(temp)) == 1 and current_max < int(temp):
                current_max = int(temp)
                rslt =  temp

        return rslt