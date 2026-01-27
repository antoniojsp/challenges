# https://leetcode.com/problems/vowel-consonant-score/
class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        v = 0
        c = 0
        vowels = set("aeiou")
        for i in s:
            if i in vowels: v+=1
            elif i.isalpha():
                c+=1
        return v//c if c > 0 else 0
