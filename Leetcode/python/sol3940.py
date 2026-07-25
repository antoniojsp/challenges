# https://leetcode.com/problems/limit-occurrences-in-sorted-array/description/

class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        count = Counter(nums)
        res = []
        for val, freq in count.items():
            if freq > k:
                res.extend([val for i in range(k)])
            else:
                res.extend([val for i in range(freq)])
        return res