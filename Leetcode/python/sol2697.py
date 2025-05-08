
# https://leetcode.com/problems/lexicographically-smallest-palindrome/description/

class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s = list(s)
        for i in range(len(s)//2):
            end_index = len(s)-1-i
            if s[i] != s[end_index]:
                smaller = min(s[i], s[end_index])
                s[i] = smaller
                s[end_index] = smaller
                # if s[i] < s[len(s)-1-i]:
                #     s[len(s)-1-i] = s[i]
                # else:
                #     s[i] = s[len(s)-1-i]
        return "".join(s)