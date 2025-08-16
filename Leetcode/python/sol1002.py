# https://leetcode.com/problems/find-common-characters/description/
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        shared = Counter(words[0])
        for i in range(1, len(words)):
            shared &= Counter(words[i])
        rslt = []
        for key, val in shared.items():
            for _ in range(val):
                rslt.append(key)
        return rslt


