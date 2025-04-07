# https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/description/
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:

        seen = {}
        for i in nums1+nums2:
            seen[i[0]] = seen.get(i[0], 0) + i[1]

        result = [[i ,j] for i, j in seen.items()]
        result.sort(key=lambda x :x[0])

        return result