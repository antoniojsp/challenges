
# https://leetcode.com/problems/kth-distinct-string-in-an-array/description/
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        seen = {}
        for index, string in enumerate(arr):
            seen[string] = seen.get(string, [])
            seen[string].append(index)
        temp = [(i, j[0]) for i, j in seen.items() if len(seen[i]) == 1]
        if len(temp) < k:
            return ""
        return temp[k-1][0]