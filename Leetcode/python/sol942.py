# https://leetcode.com/problems/di-string-match/description/
class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        start = 0
        end = len(s)
        result = [0 ] *(len(s ) +1)

        for i, ch in enumerate(s):
            if ch == "I":
                result[i] = start
                start+=1
            else:
                result[i] = end
                end-=1
            i += 1

        result[i] = start
        return result