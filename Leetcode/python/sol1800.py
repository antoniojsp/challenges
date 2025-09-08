
# https://leetcode.com/problems/maximum-ascending-subarray-sum/description/
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        if len(nums) == 1: # constraints specify that len(nums) is between 1 to 100
            return nums[0]
        start = 0
        temp = 0
        max_sum = float('-inf')
        while start < len(nums)-1:
            if nums[start] < nums[start+1]:
                temp+=nums[start]
            else:
                temp+=nums[start]
                max_sum = max(max_sum, temp)
                temp = 0
            start+=1
        else:
            if nums[start-1] < nums[start]:
                temp+=nums[start]
                max_sum = max(max_sum, temp)

        return max_sum