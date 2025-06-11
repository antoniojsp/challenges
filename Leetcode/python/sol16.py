# https://leetcode.com/problems/3sum-closest/description/
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float("inf") # equal to target, update
        suma = 0
        for i, current in enumerate(nums):
            left = i+ 1
            right = len(nums) - 1
            while left < right:
                three_sum = current + nums[left] + nums[right]
                if three_sum == target:
                    return target
                how_far_from_target = abs(target - three_sum)
                if closest > how_far_from_target:
                    closest = how_far_from_target
                    suma = three_sum

                if three_sum > target:
                    right -= 1
                else:
                    left += 1
        return suma

