
# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/


class Solution:
    def canBuildWord(self, word:str, char_string:str) -> bool:
        string_dict = Counter(char_string)
        word_dict = Counter(list(word))
        for i in word:
            if i not in string_dict:
                return False
            if i in string_dict and word_dict[i] > string_dict[i]:
                return False
        return True

    def countCharacters(self, words: List[str], chars: str) -> int:
        count = 0
        for i in words:
            if self.canBuildWord(i, chars):
                count+=len(i)
        return count