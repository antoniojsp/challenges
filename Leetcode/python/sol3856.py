# https://leetcode.com/problems/trim-trailing-vowels/
class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        final_consonant = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] not in "aeiou":
                break
            final_consonant += 1
        return s[:len(s) - final_consonant]
