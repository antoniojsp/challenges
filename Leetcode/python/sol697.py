# https://leetcode.com/problems/degree-of-an-array/
class Solution:
    def find_range_length(self, nums :list, value :int) -> int:
        left = 0
        right = len(nums) - 1
        while left < right and nums[left] !=  value:
            left+=1
        while left < right and nums[right] != value:
            right-=1

        return right - left + 1

    def findShortestSubArray(self, nums: List[int]) -> int:
        count = Counter(nums) # count
        max_freq = max(count.values()) # find max frequency value
        indexes = [key for key, val in count.items() if val == max_freq] # get keys that repeat the most
        return min(self.find_range_length(nums, i) for i in indexes)
