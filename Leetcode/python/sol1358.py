# https://leetcode.com/problems/find-the-distance-value-between-two-arrays/description/
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        invalid = 0
        for i in arr1:
            for j in arr2:
                if abs( i -j) <= d:
                    invali d+ =1
                    break
        return len(arr1) - invalid # number of valids (tha thave at least one |arr1[i]-arr2[j]| <= d)
