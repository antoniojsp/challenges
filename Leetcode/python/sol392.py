# https://leetcode.com/problems/is-subsequence/solutions/7139870/simple-by-antoniojsp-duf6/
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s: # if s is empty, then return true
            return True
        i :int = 0
        for char in t:
            if s[i] == char: # searching char by char, in order of s i+=1
            if i == len(s): # if all s is i   t in order, return true
                return True
        return False


