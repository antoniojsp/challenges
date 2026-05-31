# leetcode.com/problems/check-whether-two-strings-are-almost-equivalent/

class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        # optimal solution
        chars = [0]*26 # keep track of frequencies
        for i in word1: # add the frequencies from word1 and substract the freq from word2
            chars[ord(i)-ord('a')]+=1
        for i in word2:
            chars[ord(i)-ord('a')]-=1

        for i in chars: # if one character ends up with more than 3 chars after the substraction, then, it fails the test, else, return true.
            if abs(i) > 3:
                return False
        return True

        # w1 = Counter(word1)
        # w2 = Counter(word2)
        # chars = set(word1+word2)
        # for i in chars:
        #     left = w1[i] if i in w1 else 0
        #     right = w2[i] if i in w2 else 0
        #     if abs(left-right) > 3:
        #         return False
        # return True