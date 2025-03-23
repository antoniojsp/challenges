#https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/description/

from collections import Counter
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        if s == "":
            return True
        freq = Counter(s)
        current_value: int = None
        for i in freq.values():
            if current_value == None:
                current_value = i
            if current_value != i:
                return False
        return True