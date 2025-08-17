# https://leetcode.com/problems/find-the-array-concatenation-value/description/
class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        start = 0
        end = len(nums ) -1
        rslt = 0
        while start <= end:
            if start == end:
                rslt += nums[start]
            else:
                rslt += int(str(nums[start]) + str(nums[end]))
            start +=1
            end -=1

        return rslt
