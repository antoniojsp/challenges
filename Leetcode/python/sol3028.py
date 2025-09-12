
# https://leetcode.com/problems/ant-on-the-boundary/

class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        prefix = nums[:]
        for i in range(1, len(prefix)):
            prefix[i] = prefix[i-1]+prefix[i]
        return prefix.count(0)