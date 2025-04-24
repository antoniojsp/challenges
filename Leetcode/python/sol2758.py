# https://leetcode.com/problems/sort-vowels-in-a-string/description/
class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = [i for i in s if i in "aeiouAEIOU"]
        if len(vowels) == 0:
            return s
        vowels.sort()
        temp = list(s)
        i = 0
        abc = set("aeiouAEIOU")
        for idx, val in enumerate(temp):
            if val in abc:
                temp[idx] = vowels[i]
                i+=1

        return "".join(temp)

