class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        i = 0
        j = len(nums)-1
        result = float("inf")
        while i < j:
            result = min(result, (nums[i]+nums[j])/2)
            i+=1
            j-=1

        return result
