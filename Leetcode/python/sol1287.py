# https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        count = Counter(arr)
        quarter = len(arr) // 4
        for i, j in count.items():
            if j > quarter:
                return i


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        quarter = len(arr) // 4
        for i in range(len(arr)):
            if arr[i] == arr[i + quarter]:
                return arr[i]

