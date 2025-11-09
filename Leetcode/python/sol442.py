#  https://leetcode.com/problems/find-all-duplicates-in-an-array/
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n_duplicates: list[int] = []
        for idx, val in enumerate(nums):
            pos: int = abs(val)
            if nums[pos - 1] < 0:
                n_duplicates.append(pos)
            else:
                nums[pos - 1] *= -1

        return n_duplicates
