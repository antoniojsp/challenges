# https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/description/?envType=daily-question&envId=2025-11-17
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        index = []
        for i, j in enumerate(nums):
            if j == 1:
                index.append(i)
        for i in range(len(index)-1):
            if (index[i+1] - index[i]) <= k:
                return False
        return True