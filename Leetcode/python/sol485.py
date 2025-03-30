#  https://leetcode.com/problems/max-consecutive-ones/description/

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        current_max = 0
        count = 0
        for i in nums:
            if i == 1:
                count += 1
                if count > current_max:
                    current_max = count
            else:
                count = 0

        return current_max


