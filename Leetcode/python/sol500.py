# https://leetcode.com/problems/keyboard-row/
class Solution:

    def helper(self, word, row):
        for i in word:
            if i.lower() not in row:
                return False
        return True

    def findWords(self, words: List[str]) -> List[str]:

        first_row = "qwertyuiop"
        second_row = "asdfghjkl"
        third_row = "zxcvbnm"
        result = []
        for word in words:
            if self.helper(word ,first_row) \
                    or self.helper(word ,second_row) \
                    or self.helper(word ,third_row):
                result.append(word)

        return result
