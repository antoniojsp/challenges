
#  https://leetcode.com/problems/product-of-array-except-self/description/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        left = [1, nums[0]]
        for i in range(1,len(nums)):
            left.append(left[-1]*nums[i])
        right = [1, nums[-1]]
        for i in range(len(nums)-2, -1,-1):
            right.append(right[-1]*nums[i])
        result = []
        i = 0
        while i < len(right)-1:
            result.append( left[i] * right[len(right)-i-2] )
            i+=1

        return result
