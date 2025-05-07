
# https://leetcode.com/problems/minimum-string-length-after-removing-substrings/description/
class Solution:
    def minLength(self, s: str) -> int:
        while True:
            length = len(s)
            s = s.replace("AB", "").replace("CD", "")
            if length == len(s):
                return len(s)
