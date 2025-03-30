class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        maxi = max(nums)
        return int((maxi+maxi+k-1)*(k/2))