# https://leetcode.com/problems/relative-sort-array/description/
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count1 = Counter(arr1)
        set1 = set(arr1)
        set2 = set(arr2)
        ending = sorted(list(set 1 -set2))

        result = []
        for i in arr 2 +ending:
            result.extend([i ] *count1[i])
        return result
