# https://leetcode.com/problems/apply-operations-to-an-array/
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:

        for i in range(len(nums ) -1): # look for the condition and apply the transformation requested
            if nums[i] == nums[ i +1]:
                nums[i]*=2
                nums[ i +1] = 0
        write = 0 # setting pointers
        read = 0
        while read < len(nums): # if read points to a number > 0, then space is available for writing.
            if nums[read] != 0:
                nums[write] = nums[read]
                write+=1
            read+=1
        for i in range(write, len(nums)): # write is the space where the zeros begims
            nums[i] = 0

        return nums



