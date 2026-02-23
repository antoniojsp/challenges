
# https://leetcode.com/problems/second-largest-digit-in-a-string/description/

class Solution:
    def secondHighest(self, s: str) -> int:
        first = -1
        second = -1
        for char in s:
            if char.isdigit():
                i = int(char)
                if i > first:
                    second = first
                    first = i
                elif first > i  and i > second:
                    second = i
        return second