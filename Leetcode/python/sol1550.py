# https://leetcode.com/problems/three-consecutive-odds/description/
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:

        if len(arr) < 3:
            return False

        for i in range(0, len(arr ) -2):
            if arr[i ] % 2!=0 and arr[ i +1 ] % 2!=0 and arr[ i +2 ] % 2!=0:
                return True

        return False

