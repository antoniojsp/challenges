# https://leetcode.com/problems/rank-transform-of-an-array/description/?envType=problem-list-v2&envId=v84f01ec
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = dict() # map locations
        for i, val in enumerate(sorted(set(arr))): # make values uniques, sort them and then map them.
            rank[val] = i + 1 # plus 1 because it starts from 1st place.
        return [rank[i] for i in arr] # map each element from arr to its place

