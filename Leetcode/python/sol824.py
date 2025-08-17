#  https://leetcode.com/problems/goat-latin/description/
class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split(" ")
        vowels = set("AEIOUaeiou")
        for idx, word in enumerate(words):
            if word[0] not in vowels: # check if first letter is a vowel or consonant
                words[idx] = words[idx][1:] + word[0] # if consonant, remove first and add it to the end
            words[idx]+="ma" # all words get "ma" added
            words[idx]+="a " *(idx +1) # depending of the index, add "a" index number of times

        return " ".join(words)

