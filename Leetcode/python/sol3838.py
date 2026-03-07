
# https://leetcode.com/problems/weighted-word-mapping/

class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res:list[str] = []
        for word in words:
            total = 0
            for char in word:
                index = ord(char)-ord('a')
                total += weights[index]
            res.append(chr(ord('z') - total%26))
        return "".join(res)