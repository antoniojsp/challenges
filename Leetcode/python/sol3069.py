# https://leetcode.com/problems/distribute-elements-into-two-arrays-i/description/
class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 :list[int] = [nums[0]]
        arr2 :list[int] = [nums[1]]

        for i in range(2, len(nums)):
            last1 :int = arr1[-1]
            last2 :int = arr2[-1]
            if last1 > last2:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])

        return arr1 + arr2

