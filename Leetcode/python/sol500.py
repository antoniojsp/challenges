# https://leetcode.com/problems/keyboard-row/
class Solution:

    def helper(self, word, row):
        for i in word:
            if i.lower() not in row:
                return False
        return True

    def findWords(self, words: List[str]) -> List[str]:

        test = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        result = []
        for word in words:
            for i in test:
                if self.helper(word, i):
                    result.append(word)
                    break

        return result