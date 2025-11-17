
# https://leetcode.com/problems/find-missing-elements/

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        max_val = max(nums)
        min_val = min(nums)
        result = []
        numbers = set(nums)
        for i in range(min_val, max_val+1):
            if i not in numbers:
                result.append(i)
        return result