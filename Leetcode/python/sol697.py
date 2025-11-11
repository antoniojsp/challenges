# https://leetcode.com/problems/degree-of-an-array/
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        first_left = {}
        first_right = {}
        count = {}
        max_freq = float("-inf")
        for i in range(len(nums)):
            if nums[i] not in first_left:
                first_left[nums[i]] = i
            first_right[nums[i]] = i
            count[nums[i]] = count.get(nums[i], 0) + 1
            max_freq = max(max_freq, count[nums[i]])

        max_freq_key = [key for key, val in count.items() if val == max_freq]
        min_distance = float('inf')
        for i in max_freq_key:
            min_distance = min(min_distance, first_right[i] - first_left[i] + 1)
        return min_distance




