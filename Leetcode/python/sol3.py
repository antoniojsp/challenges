# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique :set = set()
        l :int = 0
        max_count :int = 0
        for i in range(len(s)):
            while s[i] in unique:
                unique.remove(s[l])
                l+=1
            unique.add(s[i])
            max_count = max(max_count, i - l +1)

        return max_count




