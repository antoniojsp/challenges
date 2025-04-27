# https://leetcode.com/problems/sort-characters-by-frequency/description/?envType=problem-list-v2&envId=bucket-sort

class Solution:
    def frequencySort(self, s: str) -> str:
        seen = {}
        for i in s:
            seen[i] = seen.get(i, 0) + 1

        freq = list(seen.items())
        freq.sort(key=lambda x:x[1], reverse=True)
        rslt = "".join(char*times for char, times in freq)
        return rslt