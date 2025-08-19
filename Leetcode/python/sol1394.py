# https://leetcode.com/problems/find-lucky-integer-in-an-array/description/
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = Counter(arr)
        rslt = [i for i, j in freq.items() if i == j]

        return max(rslt) if rslt else -1
