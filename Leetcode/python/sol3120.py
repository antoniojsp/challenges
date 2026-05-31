
# https://leetcode.com/problems/count-the-number-of-special-characters-i/description/

from collections import defaultdict

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count = defaultdict(int)
        rslt = 0
        for i in sorted(word):
            if i.swapcase() in count:
                rslt+=1
                del count[i.swapcase()]
            else:
                count[i]+=1

        return rslt


from collections import defaultdict

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower = set()
        upper = set()
        for i in word:
            if i.isupper():
                upper.add(i)
            else:
                lower.add(i)
        rslt = 0
        for i in upper:
            if i.swapcase() in lower:
                rslt+=1
        return rslt


class Candidate:
    def __init__(self):
        self.isUpper = False
        self.isLower = False

    def seen(self, letter):
        if letter.isupper():
            self.isUpper = True
        else:
            self.isLower = True

    def isSpecial(self):
        return self.isUpper and self.isLower


class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count = 0
        chars = {}
        for char in word:
            if char.lower() not in chars:
                chars[char.lower()] = Candidate()
            chars[char.lower()].seen(char)
        for j in chars.values():
            if j.isSpecial():
                count += 1

        return count