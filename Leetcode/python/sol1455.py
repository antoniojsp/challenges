# https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/description/
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split(" ")
        for idx, word in enumerate(words):
            if word[:len(searchWord)] == searchWord:
                return idx+1
        return -1

