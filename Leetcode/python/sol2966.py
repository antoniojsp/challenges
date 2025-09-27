# https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/solutions/7226232/greedy-by-antoniojsp-k6jk/
class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(0, len(nums), 3):
            if nums[i + 3 - 1] - nums[i] > k:
                return []
            result.append(nums[i:i + 3])

        return result

