# https://leetcode.com/problems/count-partitions-with-even-sum-difference/description/
from itertools import accumulate
class Solution:
    def left_prefix(self, nums :List[int]) -> List[int]:
        return list(accumulate(nums))
    def right_prefix(self, nums :List[int]) -> List[int]:
        return list(accumulate(nums[::-1]))[::-1]

    def countPartitions(self, nums: List[int]) -> int:
        left = self.left_prefix(nums)
        right = self.right_prefix(nums)
        count_even = 0

        for i in range(len(nums ) -1):
            if (left[i] - right[ i +1] ) % 2==0:
                count_even+=1
        return count_even

