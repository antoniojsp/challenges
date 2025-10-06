
# https://leetcode.com/problems/compute-alternating-sum/description/


class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        # rslt = 0
        # for i in range(len(nums)):
        #     if i % 2 == 0:
        #         rslt+=nums[i]
        #     else:
        #         rslt+=-nums[i]
        # return rslt
        return sum(nums[::2]) - sum(nums[1::2]) # faster than loops since it's implemented in cpython