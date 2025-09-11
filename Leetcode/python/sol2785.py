# https://leetcode.com/problems/sort-vowels-in-a-string/description/?envType=daily-question&envId=2025-09-11
class Solution:
    def sortVowels(self, s: str) -> str:
        vowels_set = set("aeiouAEIOU")
        vowels = [i for i in s if i in vowels_set]
        vowels.sort()
        string_list = list(s)
        i = len(vowels) -1
        for idx in range(len(string_list) - 1, -1, -1):
            if string_list[idx] in vowels_set:
                string_list[idx] = vowels[i]
                i -= 1

        return "".join(string_list)
