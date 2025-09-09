class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        # create reverse array, and only add non alpha chars
        reverse = [''] * len(s)
        for i in range(len(s)):
            if not s[i].isalpha():
                reverse[i] = s[i]

        s = [i for i in s if i.isalpha()]
        for i in range(len(reverse)):
            if not reverse[i]:
                reverse[i] = s.pop()

        return "".join(reverse)

