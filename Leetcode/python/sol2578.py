
# https://leetcode.com/problems/split-with-minimum-sum/description/

class Solution:
    def join_int(self, digits:list[int])->int:
        rslt = 0
        for idx, val in enumerate(digits[::-1]):
            rslt += val*(10**idx)
        return rslt

    def splitNum(self, num: int) -> int:
        nums = list(map(int, str(num)))
        nums.sort()
        num1 = []
        num2 = []
        for idx, num in enumerate(nums):
            if idx%2 == 0:
                num1 += [num]
            else:
                num2 += [num]

        return self.join_int(num1) + self.join_int(num2)
