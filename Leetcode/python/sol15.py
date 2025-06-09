
# https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i, val in enumerate(nums):
            if i > 0 and  nums[i] == nums[i-1]:
                continue
            left = i+1
            right = len(nums)-1
            while left < right:
                if val + nums[left] + nums[right] == 0:
                    while(left < right and nums[left] == nums[left+1]):
                        left+=1
                    while(left < right and nums[right] == nums[right-1]):
                        right-=1
                    temp =[val, nums[left], nums[right]]
                    result.append(temp[:])
                    right-=1
                    left+=1
                elif 0 < val + nums[left] + nums[right]:
                    right-=1
                else:
                    left+=1
        return result




