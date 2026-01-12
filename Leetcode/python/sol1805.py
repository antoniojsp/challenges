# https://leetcode.com/problems/number-of-different-integers-in-a-string/description/
class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        word = list(word)
        for i in range(len(word)):
            if not word[i].isdigit():
                word[i ] =" "
        word = "".join(word)
        word = word.split()
        return len(set(int(i) for i in word))

