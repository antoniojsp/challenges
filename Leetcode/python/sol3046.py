# https://leetcode.com/problems/split-the-array/
class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        count = Counter(nums) # count frequencies
        for freq in count.values(): # if an item appears more than twice, then the array cannot create 2 distinct sub arrays
            if freq > 2:
                return False
        return True
