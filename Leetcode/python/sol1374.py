# https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/description/


class Solution:
    def generateTheString(self, n: int) -> str:
        return "a"+"b"*(n-1) if n%2 == 0 else "a"*n