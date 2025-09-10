# https://leetcode.com/problems/longest-nice-substring/
class Solution:
    def longestNiceSubstring(self, s: str) -> str:

        def helper(substring :str):
            if len(substring) < 2: # if the substring is less than 2, then the rule cannot be aplleyed
                return ""

            char_unique = set(substring) # gets all the uniques values
            for idx, char in enumerate(substring):
                if char.swapcase() not in char_unique: # check if the char has its variant (lower or upper case) present, divide if not since that char can be discarded
                    left = helper \
                        (substring[:idx]) # divide array using the value that has no upper or lower version (variant)
                    right = helper(substring[idx+1:])
                    return left if len(left) >= len(right) else right # return longest substring

            return substring

        return helper(s)


