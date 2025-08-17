#  https://leetcode.com/problems/circular-sentence/solutions/7093244/on-by-antoniojsp-ulu4/
class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        # no checking for empty sentence due constraints

        if sentence[0] != sentence[-1]: # check that first and last char is equal, if not, return false
            return False

        words = sentence.split(" ")
        for i in range(1, len(words)):
            if words[ i -1][-1] != words[i][0]:
                return False

        return True
