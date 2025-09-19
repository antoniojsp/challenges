
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