# https://leetcode.com/problems/find-the-xor-of-numbers-which-appear-twice/

class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        temp = Counter(nums)
        rslt = 0
        for val, freq in temp.items():
            if freq == 2:
                rslt^=val
        return rslt
