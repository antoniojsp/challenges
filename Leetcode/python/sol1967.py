# https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/

class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        rslt = 0
        for i in patterns:
            if i in word:
                rslt += 1
        return rslt


