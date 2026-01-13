# https://leetcode.com/problems/reformat-the-string/description/
class Solution:
    def reformat(self, s: str) -> str:
        # separate letters and numbers
        letters = [i for i in s if i.isalpha()]
        number = [i for i in s if i.isdigit()]

        if abs(len(letters ) -len(number)) > 1: # if diff between numbers and letter, then no string can be formed.
            return ""

        result = []
        shorter ,longer = (letters, number) if len(letters) < len(number) else (number, letters)
        for i in range(len(longer)): # add one letter then one digit at the time
            result.append(longer.pop())
            if shorter:
                result.append(shorter.pop())
        return "".join(result)




