# https://leetcode.com/problems/find-the-original-typed-string-i/description/


class Solution:
    def possibleStringCount(self, word: str) -> int:
        if len(word) ==  0:
            return 0
        result = 0
        for i in range(len(word)-1):
            if  word[i] == word[i+1]:
                result+=1
        return result + 1