# https://leetcode.com/problems/subarray-sum-equals-k/description/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if len(nums) < 1:
            return 0

        prefix_sum = 0
        prefix_map = {0:1}
        count = 0

        for num in nums:
            prefix_sum+=num
            needed =  prefix_sum - k
            if needed in prefix_map:
                count += prefix_map[needed]
            sums[prefix_sum] = sums.get(prefix_sum, 0)+1
        return count

