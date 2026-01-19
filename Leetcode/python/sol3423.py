class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        result = abs(nums[0] - nums[-1])
        for i in range(len(nums) - 1):
            result = max(result, abs(nums[i] - nums[i + 1]))
        return result

        # for i in range(-1,len(nums)-1):
        #     result = max(result, abs(nums[i] - nums[i+1]))
        # return result
