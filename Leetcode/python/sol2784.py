# https://leetcode.com/problems/check-if-array-is-good/description/

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        """
        No need to check if nums is empty since constraints establish that the array, at least, contain 1 element.
        """
        n = max(nums)
        freq = Counter(nums)
        for i in range(1,n):
            if freq[i] != 1:
                return False
        return freq[n] == 2