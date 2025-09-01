#https://leetcode.com/problems/check-distances-between-same-letters/
from collections import defaultdict


class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        indexes = defaultdict(list)
        for i, char in enumerate(s):
            indexes[char].append(i)
        ans = [0 ] *26
        for i, j in indexes.items():
            ans[ord(i ) -ord('a')] = abs(j[0] - j[1]) - 1

        unique =set(s)
        for i in unique:
            index = ord(i) - ord('a')
            if ans[index] != distance[index]:
                return False
        return True
