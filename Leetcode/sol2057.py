class Solution:
    def smallestEqual(self, nums: List[int]) -> int:

        for idx, val in enumerate(nums):
            if idx % 10 == nums[idx]:
                return idx

        return -1