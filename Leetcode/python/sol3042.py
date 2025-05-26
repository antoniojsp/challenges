# leetcode.com/problems/count-prefix-and-suffix-pairs-i/

class Solution:
    def isPrefixAndSuffix(self, str1:str, str2:str) -> bool:
        if len(str1) > len(str2):
            return False
        len_str1 = len(str1)
        return str1 == str2[:len_str1] and str1 == str2[-len_str1:]

    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        rslt = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if self.isPrefixAndSuffix(words[i], words[j]):
                    rslt+=1
        return rslt