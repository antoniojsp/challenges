#  https://leetcode.com/problems/check-if-word-equals-summation-of-two-words/description/
class Solution:
    def digit_value(self, letter :chr) -> int:
        return ord(letter) - ord('a')

    def value(self, string :str):
        rslt = 0
        for i in range(len(string)):
            curr = len(string) - 1 -i
            rslt += self.digit_value(string[curr]) * (10 ** i)
        return rslt

    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        return self.value(firstWord) + self.value(secondWord) == self.value(targetWord)