# https://leetcode.com/problems/maximum-number-of-words-you-can-type/
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:

        split_text = text.split(" ") # text str is split in words.
        rslt = 0
        for word in split_text:
            for i in brokenLetters:
                if i in word:
                    rslt+=1
                    break

        return len(split_text) - rslt