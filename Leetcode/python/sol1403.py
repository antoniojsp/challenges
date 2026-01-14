
# https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order/description/?envType=problem-list-v2&envId=greedy


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        total = sum(nums)
        counted = 0
        result = []
        for i in nums:
            counted += i
            result.append(i)
            if counted > total - counted:
                break
        return result