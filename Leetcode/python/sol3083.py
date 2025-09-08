
# https://leetcode.com/problems/existence-of-a-substring-in-a-string-and-its-reverse/description/

class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        if len(s) <= 1:
            return False

        reverse = s[::-1]
        i = 0
        j = 1
        while j < len(s):
            if s[i:j+1] in reverse:
                if len(s[i:j+1]) > 1:
                    return True
                j+=1
            else:
                i+=1

        return False