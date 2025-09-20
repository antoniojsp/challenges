

# https://leetcode.com/problems/consecutive-characters/
class Solution:
    def maxPower(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        max_len = 1
        curr_len = 1
        curr = 0
        while curr < len(s)-1:
            if s[curr] == s[curr+1]:
                curr_len+=1
            else:
                curr_len = 1
            max_len = max(max_len, curr_len)
            curr+=1

        return max_len