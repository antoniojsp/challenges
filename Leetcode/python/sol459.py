# https://leetcode.com/problems/repeated-substring-pattern/
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) <= 1:
            return False

        for length in range(1, len(s )// 2 +1):
            if len(s ) %length != 0:
                continue
            check = set()
            for i in range(0, len(s), length):
                check.add(s[i: i +length])
                if len(check) > 1:
                    break
            if len(check) == 1:
                return True

        return False