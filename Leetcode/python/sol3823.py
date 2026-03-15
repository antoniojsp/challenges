
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





class Solution:
    def swap(self, res, predicate):
        l = 0
        r = len(res) - 1
        while l < r:
            while l < r and predicate(res[l]):
                l+=1
            while l < r and predicate(res[r]):
                r-=1
            res[l], res[r] = res[r], res[l]
            l+=1
            r-=1

    def reverseByType(self, s: str) -> str:
        res = list(s)
        self.swap(res, lambda x: x.isalpha())
        self.swap(res, lambda x: not x.isalpha())
        return "".join(res)
