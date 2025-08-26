# https://leetcode.com/problems/monotonic-array/solutions/7126127/on-by-antoniojsp-zgu1/
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc, dec = True, True
        for i in range(1, len(nums)):
            if nums[ i -1]  - nums[i] < 0:
                dec = False
            elif nums[ i -1] - nums[i] > 0:
                inc = False

        return inc or dec

        # if len(nums) < 2:
        #     return True
        # res = [nums[i]-nums[i+1] for i in range(len(nums)-1)]
        # if all(i <= 0 for i in res) or all(i >= 0 for i in res):
        #     return True

        # return False







