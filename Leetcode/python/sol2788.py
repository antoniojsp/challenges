# https://leetcode.com/problems/split-strings-by-separator/description/
class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:

        result = []
        for i in words:
            temp = i.split(separator)
            result += list(filter(lambda x: len(x ) >0, temp))

        return result
