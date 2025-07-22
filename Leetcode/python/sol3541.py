# https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/description/

class Solution:
    def maxFreqSum(self, s: str) -> int:
        freq = Counter(s)
        max_num_cons = 0
        max_num_vocal = 0
        vowels = set("aeiou")
        for letter, frequencies in freq.items():
            if letter in vowels:
                max_num_vocal = max(max_num_vocal, frequencies)
            else:
                max_num_cons = max(max_num_cons, frequencies)

        return max_num_cons + max_num_vocal