# https://leetcode.com/problems/remove-palindromic-subsequences/
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        # if it's already a palindrome, so jut return 1  (1 step)
        if s == s[::-1]:
            return 1
        # All other cases,you can do it in 2 steps (first remove all a and then all b)
        return 2
