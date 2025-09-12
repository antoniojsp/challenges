# https://leetcode.com/problems/points-that-intersect-with-cars/
class Solution:
    def find_max_2d(self, nums):
        max_value = float('-inf')
        for num in nums:
            max_value = max(max_value, max(num))
        return max_value

    def numberOfPoints(self, nums: List[List[int]]) -> int:
        length = self.find_max_2d(nums)
        track = [0 ] *(length +1)

        for start, end in nums:
            for i in range(start, end +1):
                track[i] = 1

        return sum(track)



class Solution:

    def numberOfPoints(self, nums: List[List[int]]) -> int:
        seen = set()

        for start, end in nums:
            for i in range(start, end+1):
                seen.add(i)

        return len(seen)
