
# https://leetcode.com/problems/valid-palindrome/description/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""
        for i in s.lower():
            if i.isalnum():
                clean+= i

        return clean == clean[::-1]