# https://leetcode.com/problems/string-matching-in-an-array/

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        # words.sort(key=lambda x:len(x)) # in case the constraints are too big
        ans = []
        for i in range(len(words)):
            for j in range(len(words)):
                if words[i] != words[j] and words[i] in words[j]:
                    ans.append(words[i])
                    break
        return ans