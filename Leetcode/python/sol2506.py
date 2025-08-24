# https://leetcode.com/problems/count-pairs-of-similar-strings/description/
class Solution:
    def similarPairs(self, words: List[str]) -> int:
        set_list = [str(sorted(set(i))) for i in words]
        # set_list = [frozenset(i) for i in words]
        freq = {}
        for i in set_list:
            freq[i] = freq.get(i, 0 ) +1
        rslt = 0
        for val in freq.values():
            rslt += (va l *(va l -1) )/ /2

        return rslt