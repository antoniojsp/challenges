# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        arr = [0] *len(nums)
        for i in nums:
            arr[i-1]+=1
        return [idx+1 for idx, val in enumerate(arr) if val == 0]



class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            to_index = abs(nums[i])-1
            if 0 < nums[to_index]:
                    nums[to_index]*=-1
        return [i+1 for i, j in enumerate(nums) if j > 0]
