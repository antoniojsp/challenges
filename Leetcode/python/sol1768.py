#  https://leetcode.com/problems/merge-strings-alternately/

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        result = []
        i = 0
        j = 0
        while i < len(word1) or i < len(word2):
            if i < len(word1):
                result.append(word1[i])
            if j < len(word2):
                result.append(word2[j])
            i += 1
            j += 1

        # if i < len(word1):
        #     result.append(word1[i:])
        # elif j < len(word2):
        #     result.append(word2[i:])

        return "".join(result)

