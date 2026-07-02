# https://leetcode.com/problems/verifying-an-alien-dictionary/


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # create rank
        ranking = {c:idx for c, idx in enumerate(order)}
        for idx, char in enumerate(order):
            ranking[char] = idx

        # check each pair if they are in order, if one is not return false, if two words have same prefix, the one who is the longest goes after
        for i in range(1, len(words)):
            for w1, w2 in zip(words[i-1], words[i]):
                if w1 == w2:
                    continue
                if ranking[w1] > ranking[w2]:
                    return False
                else:
                    break
            else:
                if len(words[i-1]) > len(words[i]) and words[i-1].startswith(words[i]):
                    return False
        return True