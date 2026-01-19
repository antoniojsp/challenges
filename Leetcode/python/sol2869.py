
# https://leetcode.com/problems/minimum-operations-to-collect-elements/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        seen = set()
        count = 0
        for i in range(len(nums)-1, -1,-1):
            if 1 <= nums[i] <= k:
                seen.add(nums[i])
            count+=1
            if len(seen) == k:
                break
        return count