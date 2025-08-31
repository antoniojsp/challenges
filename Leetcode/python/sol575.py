# https://leetcode.com/problems/distribute-candies/description/

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        half = len(candyType)//2
        types = len(set(candyType))
        return min(half, types)