#  https://leetcode.com/problems/occurrences-after-bigram/description/
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        ans = []
        words = text.split(" ")
        if len(words) < 3:
            return []
        for idx in range(len(words)):
            if idx +2 < len(words) and words[idx] == first and words[idx +1] == second:
                ans.append(words[idx +2])
        return ans
