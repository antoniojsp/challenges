# https://leetcode.com/problems/valid-word/
from string import ascii_letters, digits


class Solution:
    def is_consonant(self, word: list[str]) -> list:
        cons_set = set("aeiouAEIOU123456790")
        return [i for i in word if i not in cons_set]

    def is_vowel(self, word):
        cons_set = set("aeiouAEIOU")
        return [i for i in word if i in cons_set]

    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        cons_set = set("aeiouAEIOU123456790")
        all_chars = set(ascii_letters + digits)
        for i in word:
            if i not in all_chars:
                return False

        cons = self.is_consonant(word)
        v = set("aeiouAEIOU")
        vowels = self.is_vowel(word)
        return len(cons) > 0 and len(vowels) > 0



