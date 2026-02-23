

class Solution:
    def check(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            prev = i
            isGood = True
            for _ in range(len(nums)-1):
                if nums[prev] > nums[(prev+1)%len(nums)]:
                    isGood = False
                    break
                prev = (prev+1)%len(nums)
            if isGood:
                return True
        return False