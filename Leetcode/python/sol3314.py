# https://leetcode.com/problems/construct-the-minimum-bitwise-array-i/description/
from typing import List


class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for val in nums:
            value = -1
            for i in range(val):
                if (i | (i + 1 )) == val:
                    print("val", i , i+1)
                    value = i
                    break
            ans.append(value)
        return ans


for i in range(20):
    # if i+i+1 == i|i+1:
    print(f"{i} {bin(i)[2:]} : {i+1} {bin(i+1)[2:]} : ", i|i+1)



