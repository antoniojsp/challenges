
# https://leetcode.com/problems/count-prefixes-of-a-given-string/solutions/7114756/startwith-by-antoniojsp-0nav/

class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        count = 0
        for i in words:
            if s.startswith(i):
                count+=1
        return count