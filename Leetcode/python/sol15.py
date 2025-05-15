from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        results = []
        for i, j in enumerate(nums):
            left = i+1
            right = len(nums) - 1
            while left < right:
                # print(j,nums[left] ,nums[right])
                temp = nums[left] + nums[right] + j
                if temp == 0:
                    results.append(sorted([j, nums[left], nums[right]]))
                    right-=1
                    left+=1
                elif temp > j:
                    right -= 1
                else:
                    left += 1

        # print(results)
        rslt = []
        for i in results:
            if i not in rslt:
                rslt.append(i)

        return rslt
