
# https://leetcode.com/problems/reverse-letters-then-special-characters-in-a-string/description/

class Solution:
    def reverseByType(self, s: str) -> str:
        alpha = []
        special = []
        for i in s:
            if i.isalpha():
                alpha.append(i)
            if not i.isalpha():
                special.append(i)

        res = []
        for ch in s:
            if ch.isalpha():
                res.append(alpha.pop())
            else:
                res.append(special.pop())
        return "".join(res)