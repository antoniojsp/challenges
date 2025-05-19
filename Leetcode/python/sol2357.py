# https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/description/
class Solution:

    def min_non_zero(self, nums :list) -> int:
        min_val = float("inf")
        for i in nums:
            if i <= 0:
                continue
            min_val = min(min_val, i)
        return min_val

    def minimumOperations(self, nums: List[int]) -> int:
        rslt = 0
        while (minimo := self.min_non_zero(nums)) != float("inf") :
            for i, j in enumerate(nums):
                if j >= minimo:
                    nums[i]-=minimo
            rslt+=1

        return rslt

