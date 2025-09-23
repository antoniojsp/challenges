
# https://leetcode.com/problems/increasing-decreasing-string/description/

class Solution:
    def sortString(self, s: str) -> str:
        freq = [0]*26
        for i in s:
            freq[ord(i) - ord('a')]+=1
        result = []
        add = result.append
        remaining = len(s)
        while remaining > 0:
            for i in range(len(freq)):
                if freq[i] > 0:
                    add(i)
                    freq[i]-=1
                    remaining-=1
            for i in range(len(freq)-1, -1, -1):
                if freq[i] > 0:
                    add(i)
                    freq[i]-=1
                    remaining-=1

        return "".join(chr(i+ord('a')) for i in result)